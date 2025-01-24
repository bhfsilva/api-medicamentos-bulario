from typing import Union
from src.config.app import app, get

@get("/medicines")
async def get_medicines(search: Union[str, None] = None):
  """
  Retrieve a list of all medicines.
  
  If a search query is provided, returns a list of medicines matching the given name.
  """
  if search:
    return {"Hello": search}
  return {"Hello": "world"}


@get("/medicines/{process_number}")
async def get_medicine_by_process_number(process_number: str):
  """Retrieve detailed information about a specific medicine using its process number."""
  return {"Hello": "World"}


@get("/medicines/available/{medicine_name}")
async def get_available_medicines_by_name(medicine_name: str):
  """Retrieve a list of available medicines that match the provided name or partial name."""
  return {"Hello": "World"}
