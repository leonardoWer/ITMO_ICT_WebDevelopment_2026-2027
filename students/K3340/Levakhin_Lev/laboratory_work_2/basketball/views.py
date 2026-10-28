from django.views.generic import ListView, DetailView
from .models import Team,Match

class TeamListView(ListView):
    model = Team
    template_name = 'basketball/team_list.html'
    context_object_name = 'teams'

class TeamDetailView(DetailView):
    model = Team
    template_name = 'basketball/team_detail.html'
    context_object_name = 'team'

class MatchListView(ListView):
    model = Match
    template_name = 'basketball/match_list.html'
    context_object_name = 'matches'
    ordering = ['-date']

class MatchDetailView(DetailView):
    model = Match
    template_name = 'basketball/match_detail.html'
    context_object_name = 'match'