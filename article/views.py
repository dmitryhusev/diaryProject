from django.shortcuts import render
from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.urls import reverse
from .models import Article
from .forms import ArticleForm

def article_list(request):

    data = Article.objects.all()
    context = {'articles': data}
    return render(request, 'articles.html', context)

def add_article(request):

    if request.method != 'POST':
        form = ArticleForm()
    else:
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('articles:list'))
    context = {'form':form}
    return render(request, 'add_article.html', context)