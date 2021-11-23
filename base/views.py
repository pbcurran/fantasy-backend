from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from espn_api.basketball import League

from .products import products

# info for api calls etc
# https://github.com/cwendt94/espn-api/wiki/Basketball-Intro


def get_league_teams():
    league = League(league_id=13805593, year=2022)
    league_teams = league.teams
    teams = []
    for index, team in enumerate(league_teams):
        players = []
        
        for player in team.roster:
            # last_season_player_average = get_last_season_average(player)
            players.append({
                'playerId': player.playerId,
                'playerName': player.name,
                'currentAverage': player.avg_points,
                'injured': player.injured,
                'stats': player.stats['total_2022'],
                'projectedAverage': player.projected_avg_points
            })
        
        teams.append({
            'id': index,
            'teamName':team.team_name,
            'players': players
        })
    return teams

teams = get_league_teams()

@api_view(['GET'])
def get_league_teams(request):
    return Response(teams)
