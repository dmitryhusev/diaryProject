from django.test import TestCase
from .views import index
from django.http import HttpRequest
from article.models import Article


class TestView(TestCase):

    def test_index(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf-8')
        title = '<title>Home</title>'
        self.assertIn(title, html.replace('\n', ''))

    def test_article_q(self):
        new_article = Article()
        new_article.title = 'django'
        new_article.save()
        request = HttpRequest()
        request.GET['q'] = 'django'
        response = index(request)
        html = response.content.decode('utf-8')
        title = 'django</a>'
        self.assertIn(title, html.replace('\n', ''))

