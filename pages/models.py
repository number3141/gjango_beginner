# Определяем модели базы данных, которые Django автоматически переводит в таблицы БД

from django.db import models

# Create your models here.


class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return f"{self.text}"