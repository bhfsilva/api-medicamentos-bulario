from pydantic import BaseModel
from typing import Any, Optional
from src.models.pagination import Pagination

class HttpResponse(BaseModel):
  code: int
  status: str
  content: Any

class OkResponse(HttpResponse):
  code: int = 200
  status: str = "OK"
  content: Any
  pagination: Optional[Pagination]

class InternalServerErrorResponse(HttpResponse):
  code: int = 500
  status: str = "Internal Server Error"
  content: Any

class NoContentResponse(HttpResponse):
  code: int = 204
  status: str = "No Content"
  content: Any