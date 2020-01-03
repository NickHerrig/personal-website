import datetime

from django.db import models
from django.utils import timezone


class Essay(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, default='')
    pub_date = models.DateTimeField('date published')
    content = models.TextField()
    
    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=14)

#TODO    image = models.FilePathField(path="/img")
