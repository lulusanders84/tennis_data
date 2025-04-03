
from usta_scrapers import UAID_Scraper
import time
LEAGUE_NAME = "2025 USTA ADULT 18 & OVER - WS (WOMEN 3.0 - 18 & OVER – WS)"

def get_uaids(players: list[str], league_name: str):
    #for each team, scrape usta for each player and save uaid to csv file and wtn to another csv file
    #open team file in league dir
    with open(f"{league_name}/players_uaids.csv", "a") as player_uaids:
        scraper = UAID_Scraper()
        start_time = time.time()
        for player in players:
            print(f"Processing {player}...")
            player_name = player.replace(" ", "%20")
            #scrape player 
            attempts = 1
            uaid = None
            while uaid is None and attempts <= 5:
                print(f"attempt # {attempts}")
                uaid = scraper.scrape(player_name)
                attempts += 1
            #write player name and uaid to csv file
            print(f"Uaid found, writing to file...")
            player_uaids.write(f"{player},{uaid}\n")
        scraper.stop_scrape()
        stop_time = time.time()
        print(f"duration: {stop_time - start_time}")