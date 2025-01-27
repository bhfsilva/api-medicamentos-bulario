from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from src.models.http_responses import OkResponse, InternalServerErrorResponse

responses_models = {
  status.HTTP_200_OK: {
    "model": OkResponse,
    "description": "Ok Response"
  },
  status.HTTP_500_INTERNAL_SERVER_ERROR: {
    "model": InternalServerErrorResponse,
    "description": "Internal Server Error"
  },
  status.HTTP_422_UNPROCESSABLE_ENTITY: {
    "model": None
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
 