from django.shortcuts import render

from django.views.generic import ListView
from .models import Post
from .models import Actor

class HomePageView(ListView):
    model = Post
    template_name = "home.html"

class ActorsPageView(ListView):
    model = Actor
    template_name = "actors.html"
