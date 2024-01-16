import sys, os

sys.path.append(os.path.dirname(os.path.dirname(sys.path[0])))
from pysports.api.ncaab.conferences import Conferences
from pysports.api.ncaab.rankings import Rankings
from pysports.api.ncaab.teams import Teams

for team in Teams():
    print(team.name)
    for player in team.roster.players:
        print(player.name.encode("utf-8"))
    for game in team.schedule:
        print(game.dataframe)
        print(game.dataframe_extended)

conferences = Conferences()
print(conferences.conferences)
print(conferences.team_conference)

rankings = Rankings()
print(rankings.current)
print(rankings.current_extended)
print(rankings.complete)
