
from Scraper import Scraper
from classes import Player_Data_Getter, Player


class Players_Data():
    def __init__(self, players: list[Player], scraper: Scraper, attribute_name: str, identifier: str):
        self.players = players
        self.scraper = scraper
        self.name = attribute_name
        self.identifier = identifier
        self.players_data: list[tuple] = []
    def set_players_data_with_new_scraper(self, scraper):
        for player in self.players:
            self.scraper = scraper()
            getter = Player_Data_Getter(player, self.scraper, self.name, self.identifier)
            getter.scrape(self.players_data)
        self.scraper.stop_scrape()  
    def set_players_data(self):
        for player in self.players:
            getter = Player_Data_Getter(player, self.scraper, self.name, self.identifier)
            getter.scrape(self.players_data)
        self.scraper.stop_scrape()