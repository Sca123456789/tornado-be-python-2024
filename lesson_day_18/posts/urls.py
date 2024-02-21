from django.urls import path 
from .views import HomePageView, ActorsPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("actors.html", ActorsPageView.as_view(), name="actor")
]
