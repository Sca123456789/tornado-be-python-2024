from django.urls import path 
from .views import BlogListView, BlogDetailView, MyLogin


urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_details"),
    path("", MyLogin.as_view(), name="login"),
]