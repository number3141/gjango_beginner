# Определяем модели базы данных, которые Django автоматически переводит в таблицы БД

from django.db import models

# Create your models here.


class Post(models.Model):
    # Char хранит строку не более н символов 
    title = models.CharField(max_length=200)

    # Первый параметр указывает, с какой моделью будет создаваться связь - 
    # в данном случае это модель Company. 
    # Второй параметр - on_delete задает опцию удаления объекта текущей модели 
    # при удалении связанного объекта главной модели.
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    
    # Текст филд хранит какой-то текст 
    body = models.TextField()

    def __str__(self):
        return f"{self.title}"