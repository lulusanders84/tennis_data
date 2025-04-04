
from selenium import webdriver
from Scraper import Scraper
from abc import ABC, abstractmethod

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

class ChromeScraper(Scraper):
    options = webdriver.ChromeOptions()
    url = None
    data = {}
    
    def __init__(self):
        self.set_driver()
        self.set_start_time()
    
    def set_driver(self):
        self.driver = webdriver.Chrome(options=self.options)
    


