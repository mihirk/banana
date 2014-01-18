from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField(max_length=4096)
    timestamp = models.DateTimeField()
    author = models.CharField(max_length=64)
