from pydantic import BaseModel
from src.models.pagination import Pagination
from typing import Optional, List, Dict
from src.models.medicine import DetailedMedicine, Medicine

class HttpResponse(BaseModel):
  code: int
  status: str
  content: str | List[str] | DetailedMedicine | List[Medicine] | Dict[str, str]
  pagination: Optional[Pagination]

class OkResponse(HttpResponse):
  code: int = 200
  status: str = "OK"

class InternalServerErrorResponse(HttpResponse):
  code: int = 500
  status: str = "Internal Server Error"

class NoContentResponse(HttpResponse):
  code: int = 204
  status: str = "No Content"

class PartialContentResponse(HttpResponse):
  code: int = 206
  status: str = "Partial Content"