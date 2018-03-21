from django.test import TestCase
from .models import Article, ArticleCategory
from django.test import Client


class ModelTest(TestCase):

    def test_arcticle(self):
        art_category = ArticleCategory()
        art_category.title = 'Test article cat'
        art_category.save()
        obj = ArticleCategory.objects.get(id=1)
        self.assertEqual(obj.title, art_category.__str__())

    def test_arcticle_category(self):
        art = Article()
        art.title = 'Test article'
        self.assertEqual(art.title, art.__str__())


class ViewsTest(TestCase):

    def test_article_list(self):
        client = Client()
        response = client.get('/articles/list/')
        self.assertEqual(response.status_code, 200)

    def test_article_q(self):
        client = Client()
        response = client.get('/articles/list/', {'q': 'DJ'})
        self.assertEqual(response.status_code, 200)
