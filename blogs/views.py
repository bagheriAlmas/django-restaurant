from django.shortcuts import render

from blogs.models import Blog


def blog_list_view(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/blog_list.html', {'blogs': blogs})


def blog_detail_view(request, pk):
    blog = Blog.objects.get(pk=pk)
    last_blogs = Blog.objects.order_by('-created')[0:4]

    return render(request, 'blogs/blog_detail.html', {'blog': blog, 'last_blogs': last_blogs})
