from selenium.webdriver.common.by import By

class ScraperService():
  def __init__(self, webdriver):
    self._webdriver = webdriver

  def get_image(self, search_term: str, index: str) -> str:
    driver = self._webdriver
    base = ""

    try:
      driver.get(f"https://www.google.com/search?tbm=isch&q={search_term}")

      img = driver.find_element(By.XPATH, f"(//div[@style='position:relative']//img)[{index}]")

      if img:
        base = img.get_attribute("src").split(",")[1]

    except Exception as e:
      raise Exception(e)

    return base
