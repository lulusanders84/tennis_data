def by_league(league_name: str) -> list[tuple]:
    names_uaids = []
    with open(f"{league_name}/uaids.csv") as uaids:
        for row in uaids.read().strip().split("\n"):
            [name, uaid] = row.split(",")
            names_uaids.append((name, uaid))
    return names_uaids

def by_team(league_name: str, team_name: str) -> list[tuple]:
    players = []
    name_uaids = []
    with open(f"{league_name}/{team_name}.txt") as team_file:
        players = team_file.read().strip().split("\n")
    with open(f"{league_name}/uaids.csv") as uaids_file:
        uaids = uaids_file.read().strip().split("\n")
        for row in uaids:
            if row != "":
                [player_name, uaid] = row.split(",")
                if player_name in players:
                    name_uaids.append((player_name, uaid))
    return name_uaids