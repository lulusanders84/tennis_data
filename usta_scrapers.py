from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from ChromeScraper import ChromeScraper
from usta_site_data import data as usta_site_data
PLAYER_DISTRICT = "Colorado"

class UAID_Scraper(ChromeScraper):
    data = usta_site_data["player_search"]
    def __init__(self):
        super().__init__()

    def add_options(self):
        pass

    def set_url(self, player_name):
        self.url = self.data["url"](player_name)
   
    def scrape(self, player_name) -> str:
        self.set_url(player_name)
        self.driver.get(self.url)
        is_only = False
        try: 
            is_only = WebDriverWait(self.driver, 2).until(EC.url_contains("uaid"))
        except:
            is_only = False

        if is_only is False:
            p_elements = self.driver.find_elements(By.TAG_NAME, "p")
            district_element = None
            for p in p_elements:
                if p.text == PLAYER_DISTRICT:
                    district_element = p
                    district_element.click()
                    return re.findall(r"\d+", self.driver.current_url)[0]
            return None
        else: 
            return re.findall(r"\d+", self.driver.current_url)[0]

class WTN_Scraper(ChromeScraper):
    data = usta_site_data["wtn_search"]
    def __init__(self):
        super().__init__()

    def add_options(self):
        pass

    def set_url(self, uaid):
        self.url = self.data["url"](uaid)
   
    def scrape(self, uaid) -> str:
        self.set_url(uaid)
        self.driver.get(self.url)
        
        wtn_elements = self.driver.find_elements(By.CLASS_NAME, self.data["class_name"])
        return {"singles": wtn_elements[0].text, "doubles": wtn_elements[1].text}


