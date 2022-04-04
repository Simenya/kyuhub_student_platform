from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('resources/', views.resources),
    path('practice/', views.practice),
    path('chat/', views.chat),
     path('statistics/', views.statistics),
    path('settings/', views.settings),
    path('help/', views.help),
]
