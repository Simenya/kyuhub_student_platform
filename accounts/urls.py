from django.urls import path
from account import views
from .views import *


app_name="account"

urlpatterns = [
    path('register/', views.register, name="register"),
    # path('login/', views.login, name="login"),
]