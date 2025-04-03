from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from typing import Callable

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

def set_chrome_options():
# set up ChromeOptions
    options = webdriver.ChromeOptions()
    
    # add headless Chrome option
    options.add_argument("--window-size=1000,1000")



    return options

def get_driver(options):
    # set up Chrome in headless mode
    return webdriver.Chrome(options=options)

def scraper(url: str, scraper_func: Callable):

    # set up Chrome
    driver = get_driver(set_chrome_options())

    # open the target website
    driver.get(url)

    #perform scape functions
    results = scraper_func(driver)
    
    # close the driver instance and release its resources
    driver.quit()

    return results
