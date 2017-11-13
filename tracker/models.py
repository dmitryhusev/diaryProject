from django.db import models

# Create your models here.
class Tracker(models.Model):


    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    assignee = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s' %(self.title, self.assignee)