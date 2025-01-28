from pydantic import BaseModel

class Pagination(BaseModel):
  totalElements: int
  totalPages: int
  last: bool
  number: int
  first: bool