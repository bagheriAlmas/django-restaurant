from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=30)
    is_enabled = models.BooleanField(default=True)


class Category(models.Model):
    name = models.CharField(max_length=30)
    is_enabled = models.BooleanField(default=True)


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    content = models.TextField()
    image = models.ImageField(upload_to='blogs/', default='blog_default.png')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    categories = models.ManyToManyField('Category')
    created = models.DateTimeField(auto_now_add=True)
