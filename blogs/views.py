from django.shortcuts import render

from blogs.models import Blog
from comments.models import Comment


def blog_list_view(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/blog_list.html', {'blogs': blogs})


def blog_detail_view(request, pk):
    blog = Blog.objects.get(pk=pk)
    last_blogs = Blog.objects.order_by('-created')[0:4]
    comments = Comment.objects.filter(blog=blog).all()

    return render(request, 'blogs/blog_detail.html', {'blog': blog, 'last_blogs': last_blogs, 'comments': comments})


def blog_tag_view(request, pk):
    blogs = Blog.objects.all().filter(tags__pk=pk)
    return render(request, 'blogs/blog_list.html', {'blogs': blogs})


def blog_category_view(request, pk):
    blogs = Blog.objects.filter(categories__pk=pk).all()
    return render(request, 'blogs/blog_list.html', {'blogs': blogs})
