
from Scraper import Scraper
from classes import Player

class Player_Data_Getter():
    def __init__(self, player: Player, scraper: Scraper, attribute: str, identifier: str):
        self.player = player
        self.scraper = scraper
        self.attribute = attribute
        self.identifier = identifier
    
    def scrape(self, store: list[Player]):
        print(f"Processing {self.player.name}...")
        player_identifier = getattr(self.player, self.identifier).replace(" ", "%20")
        attempts = 1
        datum = None
        while datum is None and attempts <= 5:
            print(f"attempt # {attempts}")
            datum = self.scraper.scrape(player_identifier)
            attempts += 1
        if datum is not None:
            print(f"{self.attribute} found...")
            self.player.__setattr__(self.attribute, datum)
            store.append(self.player)
        else:
            print(f"{self.attribute} for {self.player.name} not found")
    



    