from django.shortcuts import render

from blogs.models import Blog


def blog_list_view(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/blog_list.html', {'blogs': blogs})
