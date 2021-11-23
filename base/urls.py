from django.urls import path
from . import views

urlpatterns = [
    # path('', views.getRoutes, name='routes'),
    path('leagueteams/', views.get_league_teams, name='teams'),
    #path('products/<str:pk>', views.getProduct, name='teamPlayer')
]

# command for running server you haven been using

# python manage.py runserver

