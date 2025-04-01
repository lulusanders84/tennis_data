from selenium.webdriver.common.by import By
from usta_site_data import data as usta_site_data
import re

from scraper import scraper
PLAYER_DISTRICT = "Colorado"

def scrape_uaid(player_name):
    def uaid_scraper(driver):
        p_elements = driver.find_elements(By.TAG_NAME, "p")
        district_element = None
        for p in p_elements:
            if p.text == PLAYER_DISTRICT:
                district_element = p
                district_element.click()
                return re.findall(r"\d+", driver.current_url)[0]
        return None
    
    url = f"{usta_site_data["player_search"]["url_base"]}{player_name}&page=1"
    
    return scraper(url, uaid_scraper)