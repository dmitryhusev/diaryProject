from django.conf.urls import url
from .views import main,issue

urlpatterns = [
    url(r'^tracker/$', main, name='main'),
    url(r'^issue/(?P<article_id>\d+)/$', issue, name='issue'),
]