
import from_usta
import write
from classes import Player


def uaids(players: list[Player], league_name):
    data = from_usta.get_uaids(players)
    write.append_to_file(data, f"{league_name}/uaids.csv")

def wtns(players: list[Player], league_name):
    data = [("player name", "singles", "doubles"), *from_usta.get_wtns(players)]
    write.replace_file(data, f"{league_name}/wtns.csv")

