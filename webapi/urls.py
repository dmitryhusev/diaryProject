from django.conf.urls import url
from .views import IssueList, IssueDetail

urlpatterns = [
    url(r'^issues/all/$', IssueList.as_view(), name='api_issues'),
    url(r'^issue/(?P<pk>[0-9]+)/$', IssueDetail.as_view(), name='api_issue'),

]