from typing import Union
from fastapi import Query
from src.config.app import app, get
from src.usecases.medicines import *

@get(path="/medicines/",
    description="""
    Retrieve a list of all medicines.<br><br>
    If a search query is provided, return a list of medicines that match the given name.
    """,
    swagger_url_id="getMedicines")
async def get_medicines(search: Union[str, None] = None, page: int = Query(1, gt=0), size: int = Query(5, gt=0)):
  return get_medicines_usecase(search, page, size)

@get(path="/medicines/{process_number}/",
    description="""
    Retrieve detailed information about a specific medicine using its process number.<br><br>
    If an index is provided, return the image at the corresponding position in Google Images.
    """,
    swagger_url_id="getMedicineByProcessNumber")
async def get_medicine_by_process_number(process_number: str, index: str = "1"):
  return get_medicine_by_process_number_usecase(process_number, index)

@get(path="/medicines/available/{medicine_name}/",
    description="Retrieve a list of available medicines that match the provided name or partial name.",
    swagger_url_id="getAvailableMedicinesByName")
async def get_available_medicines_by_name(medicine_name: str):
  return get_available_medicine_by_name_usecase(medicine_name)
