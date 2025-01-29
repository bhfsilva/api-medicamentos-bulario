from src.models.http_responses import *
from fastapi import FastAPI, status, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import RedirectResponse, JSONResponse

responses_models = {
  status.HTTP_200_OK: {
    "model": OkResponse,
    "description": "Ok Response"
  },
  status.HTTP_500_INTERNAL_SERVER_ERROR: {
    "model": InternalServerErrorResponse,
    "description": "Internal Server Error"
  },
  status.HTTP_206_PARTIAL_CONTENT: {
    "model": PartialContentResponse,
    "description": "Partial Content"
  },
  status.HTTP_422_UNPROCESSABLE_ENTITY: {
    "model": UnprocessableEntityResponse,
    "description": "Unprocessable Entity"
  }
}

app = FastAPI(
  title="API Medicamentos Bulário",
  version="1.0.0",
  summary="It Queries the ANVISA medicines leaflet API to retrieve comprehensive information about medicines, including details and images scraped from Google Images.",
  description="This API allows you to access detailed data on various medicines, as provided by the official ANVISA database.",
  openapi_tags=[
    {
      "name": "medicines",
      "description": "Retrieve detailed information about medicines",
    }
  ],
  redoc_url=None
)

# custom validation exception handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_: Request, exc: RequestValidationError):
  errors = exc.errors()
  field_name = errors[0]['loc'][-1]
  error_message = errors[0]['msg']

  return JSONResponse(
    status_code=422,
    content={
      "code": 422,
      "status": "Unprocessable Entity",
      "content": f"Field '{field_name}' {error_message.lower()}",
      "pagination": None
    }
  )

# redirect get request from root to /medicines
@app.get("/", include_in_schema=False)
def redirect_root():
  return RedirectResponse(url="/medicines/")

# custom get decorator
def get(path: str, description: str, swagger_url_id: str):
  def decorator(func):
    return app.get(
      path,
      tags=["medicines"],
      description=description,
      status_code=status.HTTP_200_OK,
      operation_id=swagger_url_id,
      responses=responses_models
    )(func)
  return decorator
 