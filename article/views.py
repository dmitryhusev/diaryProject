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

def edit_article(request, article_id):

    art_edit = Article.objects.get(id=article_id)
    if request.method != 'POST':
        form = ArticleForm(instance = art_edit)
    else:
        form = ArticleForm(instance = art_edit, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('articles:list'))
    context = {'form':form, 'art_edit':art_edit}
    return render(request, 'edit_article.html', context)

def delete_article(request, article_id):

    art_edit = Article.objects.get(id=article_id)
    art_edit.delete()
    return HttpResponseRedirect(reverse('articles:list'))