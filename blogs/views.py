from django.shortcuts import render

from blogs.models import Blog


def blog_list_view(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/blog_list.html', {'blogs': blogs})


def blog_detail_view(request,pk):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blogs/blog_detail.html', {'blog': blog})
