# Разрабатываем логику запроса/ответа для нашего веб-приложения 
from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from .models import Post

# Create your views here.


class HomePageView(ListView):
    # template_name - зарезервированное имя 
    template_name = 'home.html'

    model = Post

class AboutView(TemplateView):
    template_name = 'about.html'


