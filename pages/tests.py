# Предназначен для тестирования приложения 

from django.contrib.auth import get_user_model
from django.http import response
from django.test import TestCase

# Simple т.к. не используем БД
from django.test import SimpleTestCase

from .models import Post

# Create your tests here.


class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'test', 
            email = 'test@mail.com',
            password = '1234'
        )

        self.post = Post.objects.create(
            title = 'test_post', 
            body = '124',
            author = self.user
        )
    
    def test_string_repr(self):
        post = Post(title='sample')
        self.assertEqual(str(post), post.title)
    
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'test_post')    
