
from usta_scrapers import UAID_Scraper, WTN_Scraper
import write
from Scraper import Scraper
from classes import Players_Data, Player, Player_Builder
from classes.Player_Builder import Name_UAID

def get_uaids(player_names: list[str]):
    scraper = UAID_Scraper()
    store = get_data(player_names, scraper, "uaid", "name")
    data = []
    for player in store:
        data.append((player.name, player.uaid))
    return data

def get_wtns(player_info: list[Name_UAID]):
    scraper = WTN_Scraper
    store = get_data(player_info, scraper, "wtn", "uaid", scraper_per_player=True)
    data = []
    for player in store:
        data.append((player.name, player.wtn["singles"], player.wtn["doubles"]))
    return data
    
def get_data(player_info: list[str | Name_UAID], scraper: Scraper, datatype: str, player_identifier: str, scraper_per_player: bool=False) -> None:
    players = Player_Builder().build_players(player_info)
    getter = Players_Data(players, scraper, datatype, player_identifier)
    if scraper_per_player:
        getter.set_players_data_with_new_scraper(scraper)
    else:
        getter.set_players_data()
    return getter.players_data
   


            

