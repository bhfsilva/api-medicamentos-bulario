from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_webdriver():
  try:
    chrome_options = Options() 
    chrome_options.add_argument('--headless=new')
    chrome_options.binary_location='/opt/chrome/chrome-linux64/chrome'
    driver = webdriver.Chrome(
      service=Service('/opt/chromedriver-linux64/chromedriver'),
      options=chrome_options
    )
    return driver

  except Exception as e:
    raise Exception(e)
