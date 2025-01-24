from fastapi import FastAPI, status

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

# custom get decorator
def get(path: str):
  def decorator(func):
    return app.get(
      path,
      tags=["medicines"],
      status_code=status.HTTP_200_OK
      )(func)
  return decorator