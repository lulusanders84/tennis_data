
from usta_scrapers import UAID_Scraper, WTN_Scraper
import write
from Scraper import Scraper
from classes import Players_Data, Player, Player_Builder
from classes.Player_Builder import Name_UAID
import requests
from usta_site_data import data as usta_site_data

def get_uaids(players: list[Player]):
    scraper = UAID_Scraper()
    store = get_data(players, scraper, "uaid", "name")
    data = []
    for player in store:
        data.append((player.name, player.uaid))
    return data

def get_wtns(player_info: list[Player]):
    html_elements = []
    for player in player_info:
        html_elements.append((player, requests.get(usta_site_data["wtn_search"]["url"](player.uaid))))
    for element in html_elements:
        #add beautiful soup parsing

    
def get_data(players: list[Player], scraper: Scraper, datatype: str, player_identifier: str, scraper_per_player: bool=False) -> list[Player]:
    getter = Players_Data(players, scraper, datatype, player_identifier)
    if scraper_per_player:
        getter.set_players_data_with_new_scraper(scraper)
    else:
        getter.set_players_data()
    return getter.players
   


            

