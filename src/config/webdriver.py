import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_webdriver():
  try:
    config = configparser.ConfigParser()
    config.read('application.ini')

    section = 'paths'
    chrome_path_config = 'chrome_path'
    chromedriver_path_config = 'chromedriver_path'
    have_chrome_path = config.has_option(section, chrome_path_config)
    have_chromedriver_path = config.has_option(section, chromedriver_path_config)

    if not have_chrome_path or not have_chromedriver_path:
      raise Exception('Error configuring webdriver: Unable to locate the binary paths in application.ini file')
    
    chrome_options = Options() 
    chrome_options.add_argument('--headless=new')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = config.get(section, chrome_path_config)
    driver = webdriver.Chrome(
      service=Service(executable_path=config.get(section, chromedriver_path_config)),
      options=chrome_options
    )
    return driver

  except Exception as e:
    raise Exception(e)
