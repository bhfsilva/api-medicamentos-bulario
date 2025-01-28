import requests

class HttpService:
  def __init__(self, headers: dict):
    self.headers = headers

  def get(self, url: str) -> dict:
    content = {}
    response = requests.get(url, headers=self.headers)
    
    try:
      content = response.json()
    except ValueError:
      raise Exception("No JSON content")
    
    return content
