from django.contrib import admin
from .models import Article, ArticleCategory

# These models will be displayed on admin panel

admin.site.register(Article)
admin.site.register(ArticleCategory)
