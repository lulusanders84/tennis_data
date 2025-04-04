
from abc import ABC, abstractmethod
from dataclasses import dataclass
from classes import Player

@dataclass
class Name_UAID():
    name: str
    uaid: str

def build_Name_UAID(name: str, uaid: str):
    return Name_UAID(name, uaid)

class Player_Builder():
    
    @staticmethod
    def build_players(players_info: list[str | Name_UAID]) -> list[Player]:
        if isinstance(players_info[0], str):
            return Player_Builder().build_players_from_name(players_info)
        if isinstance(players_info[0], Name_UAID):
            return Player_Builder().build_players_from_name_uaids(players_info)
    
    @staticmethod
    def build_players_from_name(players: list[str]) -> list[Player]:
        return [Player(name) for name in players]

    @staticmethod
    def build_players_from_name_uaids(players: list[Name_UAID]) -> list[Player]:
        new_players = []
        for player in players:
            print(player.uaid)
            new_player = Player(player.name)
            new_player.__setattr__("uaid", player.uaid)
            new_players.append(new_player)
        return new_players



