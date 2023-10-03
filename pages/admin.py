# Файл конфигурации для встроенного приложения 

from django.contrib import admin

# Register your models here.

from .models import Post


# Отображать в админке таблицу пост
admin.site.register(Post)