import requests
from requests.exceptions import RequestException

class HttpService:
  def __init__(self, headers: dict):
    self.headers = headers

  def get(self, url: str) -> dict:
    try:
      content = {}
      response = requests.get(url, headers=self.headers)    
      response.raise_for_status()
      content = response.json()
    
    except RequestException as e:
      raise Exception(f"{str(e)}")

    except ValueError:
      raise Exception("No JSON content")
    
    return content
