
from usta_scrapers import WTN_Scraper
import read_file.uaids
import from_usta
from classes.Player_Builder import build_Name_UAID
import league
LEAGUE_NAME = "2025 USTA ADULT 18 & OVER - WS (WOMEN 3.0 - 18 & OVER – WS)"

def main():
    league.refresh_league(LEAGUE_NAME)
            
if __name__ == "__main__":
    main()