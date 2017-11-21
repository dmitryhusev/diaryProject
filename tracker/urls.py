from django.conf.urls import url
from .views import main, issues, edit_issue, add_issue

urlpatterns = [
    url(r'^tracker/$', main, name='main'),
    url(r'^issues/$', issues, name='issues'),
    url(r'^edit/issue/(?P<issue_id>\d+)/$', edit_issue, name='edit_issue'),
    url(r'^add/issue/$', add_issue, name='add_issue'),
]
