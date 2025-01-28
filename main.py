from typing import Union
from src.config.app import app, get
from src.config.webdriver import get_webdriver
from src.services.scraper import ScraperService
from src.models.http_responses import OkResponse, NoContentResponse, InternalServerErrorResponse
from src.models.pagination import Pagination
from src.services.http_client import HttpService

http_headers = {
  'Authorization': 'Guest',
  'Accept': 'application/json, text/plain, */*',
  'Referer': 'https://consultas.anvisa.gov.br'
}

http_client = HttpService(headers=http_headers)

driver = get_webdriver()

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
      return NoContentResponse(content=[])

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
    return InternalServerErrorResponse(content={"error": f"{str(e)}"})

@get(path="/medicines/{process_number}/",
    description="""
    Retrieve detailed information about a specific medicine using its process number.<br><br>
    If an index is provided, return the image at the corresponding position in Google Images.
    """,
    swagger_url_id="getMedicineByProcessNumber")
async def get_medicine_by_process_number(process_number: str, index: str = "1"):
  try:
    response = http_client.get(f"https://consultas.anvisa.gov.br/api/consulta/medicamento/produtos/?filter[numeroProcesso]={process_number}")

    if not response["content"]:
      return NoContentResponse(content=[])

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
    return InternalServerErrorResponse(content={"error": f"{str(e)}"})

@get(path="/medicines/available/{medicine_name}/",
    description="Retrieve a list of available medicines that match the provided name or partial name.",
    swagger_url_id="getAvailableMedicinesByName")
async def get_available_medicines_by_name(medicine_name: str):
  try:
    response = http_client.get(f"https://consultas.anvisa.gov.br/api/produto/listaMedicamentoBula/{medicine_name}")
    
    if not response:
      return NoContentResponse(content=[])
    
    return OkResponse(content=response, pagination=None)
  
  except Exception as e:
    return InternalServerErrorResponse(content={"error": f"{str(e)}"})
