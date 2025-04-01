from usta_scrapers import scrape_uaid
from get_teams_by_league import get_teams_by_league

def main():
    teams = get_teams_by_league("2025 USTA ADULT 18 & OVER - WS (WOMEN 3.0 - 18 & OVER – WS)")
    print(teams)
    player_name = "Lucy%20Sanders"
    #uaid = scrape_uaid(player_name)
    #print(uaid)

if __name__ == "__main__":
    main()