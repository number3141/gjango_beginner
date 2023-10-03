# Разрабатываем логику запроса/ответа для нашего веб-приложения 

from re import template
from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    # template_name - зарезервированное имя 
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'
