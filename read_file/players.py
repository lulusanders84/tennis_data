from get_teams_by_league import get_teams_by_league

def by_league(league_name: str) -> list[str]:
    teams = get_teams_by_league(league_name)
    players = []
    for team in teams:
        players = [*players, *by_team(league_name, team)]
    return players

def by_team(league_name: str, team_name: str) -> list[str]:
    players = []
    with open(f"{league_name}/{team_name}.txt") as team_file:
        players = [*players, *team_file.read().strip().split("\n")]
    return players

