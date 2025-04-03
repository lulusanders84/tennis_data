
from selenium.webdriver.remote.webdriver import WebDriver
from abc import ABC, abstractmethod

class Scraper(ABC):

    driver: WebDriver

    @abstractmethod
    def set_url(self):
        pass
    
    @abstractmethod
    def set_driver(self):
        pass

    @abstractmethod
    def scrape(self):
        pass

    @abstractmethod
    def add_options(self):
        pass

    def stop_scrape(self):
        self.driver.quit()

