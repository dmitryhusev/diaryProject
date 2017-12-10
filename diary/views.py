from django.shortcuts import render
from article.models import Article
from tracker.models import Tracker

def index(request):

    query = request.GET.get('q')
    if query:
        articles = Article.objects.filter(title__icontains=query)
    else:
        articles = Article.objects.order_by('-date_added')[:15]
    issues = Tracker.objects.order_by('-date_added')[:10]
    context = {'articles': articles, 'issues': issues}
    return render(request, "index.html", context)
