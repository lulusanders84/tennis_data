import read_file.uaids
import refresh_data
from classes.Player_Builder import build_Name_UAID

def refresh_league(league_name: str):
    player_names_uaids = read_file.uaids.by_league(league_name)
    players_info = [build_Name_UAID(info[0], info[1]) for info in player_names_uaids] 
    refresh_data.wtns(players_info, league_name)

