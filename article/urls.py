from django.conf.urls import url
from .views import article_list, add_article, edit_article,\
delete_article, view_article, add_category, delete_category, edit_category

urlpatterns = [
    url(r'^list/$', article_list, name='list'),
    url(r'^add/article/$', add_article, name='add_article'),
    url(r'^edit/article/(?P<article_id>\d+)/$', edit_article, name='edit_article'),
    url(r'^delete/article/(?P<article_id>\d+)/$', delete_article, name='delete_article'),
    url(r'^view/article/(?P<article_id>\d+)/$', view_article, name='view_article'),
    url(r'^add/category/$', add_category, name='add_category'),
    url(r'^category/(?P<category_id>\d+)/$', edit_category, name='edit_category'),
    url(r'^delete/category/(?P<category_id>\d+)/$', delete_category, name='delete_category'),
    

]