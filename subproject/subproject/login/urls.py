from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name="login_home"),
    path('check/', views.check, name="check"),
]