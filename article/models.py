from django.db import models


class Article(models.Model):


    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.FileField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s ' %(self.title)
