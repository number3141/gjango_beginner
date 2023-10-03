# Разрабатываем логику запроса/ответа для нашего веб-приложения 

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def home_page_view(request):
    return HttpResponse("Hello, World!")
