from django.core.paginator import Paginator
from django.shortcuts import render

from blogs.models import Blog
from comments.models import Comment


def blog_list_view(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blogs/blog_list.html', {'blogs': page_obj})


def blog_detail_view(request, pk):
    blog = Blog.objects.get(pk=pk)
    last_blogs = Blog.objects.order_by('-created')[0:4]
    comments = Comment.objects.filter(blog=blog).all()

    return render(request, 'blogs/blog_detail.html', {'blog': blog, 'last_blogs': last_blogs, 'comments': comments})


def blog_tag_view(request, pk):
    blogs = Blog.objects.all().filter(tags__pk=pk)
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blogs/blog_list.html', {'blogs': page_obj})


def blog_category_view(request, pk):
    blogs = Blog.objects.filter(categories__pk=pk).all()
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blogs/blog_list.html', {'blogs': page_obj})


def search_view(request):
    try:
        if request.method == 'GET':
            str_search = request.GET.get('search')
            blogs = Blog.objects.filter(title__icontains=str_search)
            paginator = Paginator(blogs, 6)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'blogs/blog_list.html', {'blogs': page_obj})
    except:
        return render(request, 'foods/food_list.html', {})
