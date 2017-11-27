from django.db import models


class ArticleCategory(models.Model):

    
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'ArtCategories'

    def __str__(self):
        return self.title




class Article(models.Model):

    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=150)
    body = models.TextField()
    image = models.FileField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s' %(self.title)

