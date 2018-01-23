from django.db import models


class Tracker(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    assignee = models.CharField(max_length=35)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '%s' % (self.title)
