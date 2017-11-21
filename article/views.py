from django.shortcuts import render
from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.urls import reverse
from .models import Article
from .forms import ArticleForm

def article_list(request):
         
    if 'q' in request.GET:
        q = request.GET['q']
        data = Article.objects.filter(title__icontains=q)
    else:
        data = Article.objects.all()
    context = {'articles': data}
    return render(request, 'articles.html', context)


def add_article(request):

    if request.method != 'POST':
        form = ArticleForm()
    else:
        form = ArticleForm(request.POST, request.FILES)
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
        form = ArticleForm(instance = art_edit, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('articles:list'))
    context = {'form':form, 'art_edit':art_edit}
    return render(request, 'edit_article.html', context)

def delete_article(request, article_id):

    art_edit = Article.objects.get(id=article_id)
    art_edit.delete()
    return HttpResponseRedirect(reverse('articles:list'))

def view_article(request, article_id):
    
    art_view = Article.objects.get(id=article_id)
    context = {'title': art_view.title, 'body': art_view.body, 'image': art_view.image}
    return render(request, 'view_article.html', context)

