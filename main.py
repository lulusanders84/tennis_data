
from usta_scrapers import WTN_Scraper
import read_file.uaids
import from_usta
from classes.Player_Builder import build_Name_UAID
import league
import refresh_data
from classes import Player
LEAGUE_NAME = "2025 USTA ADULT 18 & OVER - WS (WOMEN 3.0 - 18 & OVER – WS)"

def main():
    #league.refresh_league(LEAGUE_NAME)
    player = Player("Karen Kelley")
    player.__setattr__("uaid", "2010264023")
    refresh_data.wtns([player], LEAGUE_NAME)

if __name__ == "__main__":
    main()