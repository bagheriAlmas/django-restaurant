from django.contrib import admin
from .models import Blog, Tag, Category

admin.site.register(Blog, )
admin.site.register(Category)
admin.site.register(Tag)
