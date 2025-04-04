from selenium.webdriver.remote.webdriver import WebDriver
from abc import ABC, abstractmethod
import time


class Scraper(ABC):
    driver: WebDriver
    start_time = 0
    stop_time = 0

    @abstractmethod
    def set_url(self):
        pass

    @abstractmethod
    def set_driver(self):
        pass

    @abstractmethod
    def scrape(self, player_identifier: str):
        pass

    @abstractmethod
    def add_options(self):
        pass

    def set_start_time(self):
        self.start_time = time.time()

    def set_stop_time(self):
        self.stop_time = time.time()
        self.set_duration()

    def set_duration(self):
        self.duration = self.stop_time - self.start_time

    def stop_scrape(self):
        self.driver.quit()
        self.set_stop_time()