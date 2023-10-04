# Разрабатываем логику запроса/ответа для нашего веб-приложения 
from django.shortcuts import render

from django.views.generic import DetailView, TemplateView, ListView

from .models import Post

# Create your views here.


class HomePageView(ListView):
    # template_name - зарезервированное имя 
    template_name = 'home.html'
    model = Post

# Detal - на страницу "упадут" какие-то данные в виде отдельного объекта
class PostDet(DetailView):
    template_name = 'post.html'
    model = Post
    context_object_name = 'post'

class AboutView(TemplateView):
    template_name = 'about.html'





