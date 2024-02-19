from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from .views import ArticleListView

from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
)

urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), ),
    path("<int:pk/delete/", ArticleDeleteView.as_view(), name="article_delete")
]
