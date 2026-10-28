from django.urls import path
from . import views

app_name = 'basketball'

urlpatterns = [
    path('', views.TeamListView.as_view(), name='team_list'),
    path('team/<int:pk>/', views.TeamDetailView.as_view(), name='team_detail')
]