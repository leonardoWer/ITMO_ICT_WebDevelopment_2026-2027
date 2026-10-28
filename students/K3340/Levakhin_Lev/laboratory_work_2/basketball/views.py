from django.views.generic import ListView, DetailView
from .models import Team,Match
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

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


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('basketball:team_list')
    else:
        form = CustomUserCreationForm()

    return render(request, 'basketball/register.html', {'form': form})