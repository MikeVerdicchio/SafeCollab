from django.db import models


class Article(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()

def __unicode__(self):
    return self.title

# Create your models here.
