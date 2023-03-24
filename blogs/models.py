from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field


class Tag(models.Model):
    name = models.CharField(max_length=30)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    content = CKEditor5Field('Text', config_name='extends')
    image = models.ImageField(upload_to='blogs/', default='blog_default.png')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag',related_name='Tags')
    categories = models.ManyToManyField('Category')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
