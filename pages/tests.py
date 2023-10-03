# Предназначен для тестирования приложения 

from django.http import response
from django.test import TestCase

# Simple т.к. не используем БД
from django.test import SimpleTestCase

# Create your tests here.


class SimpleTest(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)