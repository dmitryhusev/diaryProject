from django.shortcuts import render
from article.models import Article
from tracker.models import Tracker

def index(request):

    articles = Article.objects.all()
    issues = Tracker.objects.all()
    context = {'articles': articles, 'issues': issues}
    return render(request, "index.html", context)