from django.conf.urls import url
from .views import article_list, add_article

urlpatterns = [
    url(r'^list/$', article_list, name='list'),
    url(r'^add_article/$', add_article, name='add_article'),

]