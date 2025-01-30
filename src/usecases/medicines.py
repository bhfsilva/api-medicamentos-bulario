from src.models.http_responses import *
from src.models.pagination import Pagination
from src.config.webdriver import get_webdriver
from src.services.scraper import ScraperService
from src.models.medicines import DetailedMedicine
from src.services.http_client import HttpService

http_headers = {
  'Authorization': 'Guest',
  'Accept': 'application/json, text/plain, */*',
  'Referer': 'https://consultas.anvisa.gov.br'
}
http_client = HttpService(headers=http_headers)

def get_available_medicine_by_name_usecase(name: str):
  try:
    response = http_client.get(f"https://consultas.anvisa.gov.br/api/produto/listaMedicamentoBula/{name}")
    
    if not response:
      return NoContentResponse(content=[], pagination=None)
    
    return OkResponse(content=response, pagination=None)
  
  except Exception as e:
    return InternalServerErrorResponse(content={"Error": f"{str(e)}"}, pagination=None)
  
def get_medicines_usecase(search: str | None, page: int, size: int):
  endpoint = "https://consultas.anvisa.gov.br/api/consulta/bulario/?filter[nomeProduto]="
  pagination_query = f"&page={page}&size={size}"
  try:
    response = http_client.get(f"{endpoint}{pagination_query}")

    if search:
      response = http_client.get(f"{endpoint}{search}{pagination_query}")

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

def get_medicine_by_process_number_usecase(process_number: str, index: str):
  try:
    driver = get_webdriver()
    scraper = ScraperService(webdriver=driver)
    detailed_response = http_client.get(f"https://consultas.anvisa.gov.br/api/consulta/medicamento/produtos/?filter[numeroProcesso]={process_number}")

    if not detailed_response["content"]:
      return NoContentResponse(content=[], pagination=None)
    
    medicine = detailed_response["content"][0]
    medicine_register_number = medicine["produto"]["numeroRegistro"]

    additional_info_response = http_client.get(f"https://consultas.anvisa.gov.br/api/consulta/bulario/?filter[numeroRegistro]={medicine_register_number}")

    patient_leaflet_id = ""
    professional_leaflet_id = ""

    if additional_info_response["content"]:
      simple_medicine = additional_info_response["content"][0]
      patient_leaflet_id = simple_medicine["idBulaPacienteProtegido"]
      professional_leaflet_id = simple_medicine["idBulaProfissionalProtegido"]

    medicine_name = medicine["produto"]["nome"]
    pharmaceutical_company_name = medicine["empresa"]["razaoSocial"]
    search_medicine_image_term = f"medicamento {medicine_name} {pharmaceutical_company_name}"
    medicine_image = scraper.get_image(search_medicine_image_term, index)

    driver.quit()

    return OkResponse(content=DetailedMedicine(
      ordem=medicine["ordem"],
      imagemMedicamento=medicine_image,
      idBulaPaciente=patient_leaflet_id,
      idBulaProfissional=professional_leaflet_id,
      medicamento=medicine["produto"],
      empresaFarmaceutica=medicine["empresa"],
      processo=medicine["processo"],
    ),
    pagination=None)
    
  except Exception as e:
    return InternalServerErrorResponse(content={"Error": f"{str(e)}"}, pagination=None)