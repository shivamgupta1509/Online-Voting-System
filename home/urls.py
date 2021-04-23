from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('home', views.index, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),  
    path('voteSelection', views.voteSelection, name="voteSelection"),
    path('voterInput', views.voterInput, name="voterInput"), 
    path('ballot', views.ballot, name="ballot"),
]


