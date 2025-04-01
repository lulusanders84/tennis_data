def get_teams_by_league(league_name):
    with open("teams.csv") as teams_file:
        contents = teams_file.read()
        leagues = contents.strip().split("\n")
        for league in leagues:
            row_list = league.strip(",").split(",")
            if row_list[0] == league_name:
                return row_list[1:]


