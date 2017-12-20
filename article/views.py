from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Article, ArticleCategory
from .forms import ArticleForm, ArticleCategoryForm
from django.contrib.auth.decorators import login_required

def article_list(request):
         
    if 'q' in request.GET:
        q = request.GET['q']
        data = Article.objects.filter(title__icontains=q).order_by('-date_added')
        categories = ArticleCategory.objects.order_by('title')
    else:
        data = Article.objects.order_by('-date_added')
        categories = ArticleCategory.objects.order_by('title')

    context = {'articles': data, 'categories': categories}
    return render(request, 'articles.html', context)

@login_required
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
    context = {'title': art_view.title,
                'body': art_view.body,
                'image': art_view.image,
                'article_id': article_id}
    return render(request, 'view_article.html', context)


def category(request, category_id):
    category = ArticleCategory.objects.get(id=category_id)
    category_articles = Article.objects.filter(category=category_id)
    context = {'title': category.title, 'category_id': category_id, 'articles':category_articles}
    return render(request, 'category.html', context)



def add_category(request):

    if request.method == 'POST':
        form = ArticleCategoryForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.title = instance.title.capitalize() 
            instance.save()
        return HttpResponseRedirect(reverse('articles:list'))
    else:
        form = ArticleCategoryForm()
    context = {'form': form}
    return render(request, 'add_category.html', context)

def edit_category(request, category_id):

    instance = ArticleCategory.objects.get(id=category_id)
    if request.method == 'POST':
        form = ArticleCategoryForm(instance = instance, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('articles:category', args=[category_id]))
    else:
        form = ArticleCategoryForm(instance=instance)
    context = {'form':form, 'category_id':category_id}
    return render(request, 'edit_category.html', context)


def delete_category(request, category_id):

    cat_delete = ArticleCategory.objects.get(id=category_id)
    cat_delete.delete()
    return HttpResponseRedirect(reverse('articles:list'))

