from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Post

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm

class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_details.html"

class MyLogin(LoginView):
    redirect_authenticated_user = True

    def  get_success_url(self):
        return reverse_lazy('tasks')

    def form_invaled(self, form):
        messages.error(self.request, 'Invaled user or password')
        return self.render_to_+response(self.get_context_data(form-form))