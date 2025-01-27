from typing import Union
from src.config.app import app, get
from src.config.webdriver import get_webdriver
from src.services.scraper import ScraperService
from src.services.http_client import HttpService

http_headers = {
  'Authorization': 'Guest',
  'Accept': 'application/json, text/plain, */*',
  'Referer': 'https://consultas.anvisa.gov.br'
}

client = HttpService(headers=http_headers)

driver = get_webdriver()

@get(path="/medicines/", description="Retrieve a list of all medicines.<br><br>If a search query is provided, return a list of medicines that match the given name.", swagger_url_id="getMedicines")
async def get_medicines(search: Union[str, None] = None):
  if search:
    return {"Hello": search}

  scraper = ScraperService(webdriver=driver)
  return scraper.get_image("example")

@get(path="/medicines/{process_number}/", description="Retrieve detailed information about a specific medicine using its process number.", swagger_url_id="getMedicineByProcessNumber")
async def get_medicine_by_process_number(process_number: str):
  return {"Hello": process_number}

@get(path="/medicines/available/{medicine_name}/", description="Retrieve a list of available medicines that match the provided name or partial name.", swagger_url_id="getAvailableMedicinesByName")
async def get_available_medicines_by_name(medicine_name: str):
  return {"Hello": "World"}
