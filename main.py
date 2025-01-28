from typing import Union, List
from src.config.app import app, get
from src.models.pagination import Pagination
from src.config.webdriver import get_webdriver
from src.services.scraper import ScraperService
from src.services.http_client import HttpService
from src.models.medicine import DetailedMedicine, Medicine
from src.models.http_responses import OkResponse, NoContentResponse, InternalServerErrorResponse

http_headers = {
  'Authorization': 'Guest',
  'Accept': 'application/json, text/plain, */*',
  'Referer': 'https://consultas.anvisa.gov.br'
}

http_client = HttpService(headers=http_headers)

@get(path="/medicines/",
    description="""
    Retrieve a list of all medicines.<br><br>
    If a search query is provided, return a list of medicines that match the given name.
    """,
    swagger_url_id="getMedicines")
async def get_medicines(search: Union[str, None] = None):
  endpoint = "https://consultas.anvisa.gov.br/api/consulta/bulario/?filter[nomeProduto]="
  try:
    response = http_client.get(endpoint)

    if search:
      response = http_client.get(f"{endpoint}{search}")

    if not response["content"]:
      return NoContentResponse(content=[], pagination=None)

    return OkResponse(
      content=response["content"],
      pagination=Pagination(
        totalElements=response["totalElements"],
        totalPages=response["totalPages"],
        last=response["last"],
        number=response["number"],
        first=response["first"]
      )
    )
    
  except Exception as e:
    return InternalServerErrorResponse(content={"Error": f"{str(e)}"}, pagination=None)

@get(path="/medicines/{process_number}/",
    description="""
    Retrieve detailed information about a specific medicine using its process number.<br><br>
    If an index is provided, return the image at the corresponding position in Google Images.
    """,
    swagger_url_id="getMedicineByProcessNumber")
async def get_medicine_by_process_number(process_number: str, index: str = "1"):
  driver = get_webdriver()
  scraper = ScraperService(webdriver=driver)

  try:
    detailed_response = http_client.get(f"https://consultas.anvisa.gov.br/api/consulta/medicamento/produtos/?filter[numeroProcesso]={process_number}")

    if not detailed_response["content"]:
      return NoContentResponse(content=[], pagination=None)
    
    medicine = detailed_response["content"][0]
    medicine_register_number = medicine["produto"]["numeroRegistro"]

    # get other infos like id bulario
    # simple_response = http_client.get(f"https://consultas.anvisa.gov.br/api/consulta/bulario/?filter[numeroRegistro]={medicine_register_number}")

    medicine_name = medicine["produto"]["nome"]
    pharmaceutical_company_name = medicine["empresa"]["razaoSocial"]
    search_medicine_image_term = f"medicamento {medicine_name} {pharmaceutical_company_name}"
    medicine_image = scraper.get_image(search_medicine_image_term, index)

    driver.quit()

    return OkResponse(content=DetailedMedicine(
      ordem=medicine["ordem"],
      imagem=medicine_image,
      produto=medicine["produto"],
      empresa=medicine["empresa"],
      processo=medicine["processo"],
    ),
    pagination=None)
    
  except Exception as e:
    return InternalServerErrorResponse(content={"Error": f"{str(e)}"}, pagination=None)

@get(path="/medicines/available/{medicine_name}/",
    description="Retrieve a list of available medicines that match the provided name or partial name.",
    swagger_url_id="getAvailableMedicinesByName")
async def get_available_medicines_by_name(medicine_name: str):
  try:
    response = http_client.get(f"https://consultas.anvisa.gov.br/api/produto/listaMedicamentoBula/{medicine_name}")
    
    if not response:
      return NoContentResponse(content=[], pagination=None)
    
    return OkResponse(content=response, pagination=None)
  
  except Exception as e:
    return InternalServerErrorResponse(content={"Error": f"{str(e)}"}, pagination=None)
