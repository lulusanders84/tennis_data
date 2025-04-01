from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

def set_chrome_options():
# set up ChromeOptions
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    
    # add headless Chrome option
    options.add_argument("--headless-new")
    return options

def get_driver(options):

    # set up Chrome in headless mode
    return webdriver.Chrome(options=options)

def scraper(url, scrape_func):
    # set up Chrome
    driver = get_driver(set_chrome_options())

    # open the target website
    driver.get(url)

    #perform scape function
    results = scrape_func(driver)

    # close the driver instance and release its resources
    driver.quit()

    return results