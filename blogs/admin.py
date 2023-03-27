from django.contrib import admin
from .models import Blog, Tag, Category, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created')
    filter_horizontal = ['tags', 'categories']
    list_filter = ['categories',]


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)