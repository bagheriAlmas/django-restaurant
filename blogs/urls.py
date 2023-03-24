from django.urls import path
from .views import blog_list_view, blog_detail_view, blog_tag_view, blog_category_view,search_view

urlpatterns = [
    path('blogs/', blog_list_view, name='blog_list_view'),
    path('blogs/<int:pk>', blog_detail_view, name='blog_detail_view'),
    path('tag/<int:pk>', blog_tag_view, name='blog_tag_view'),
    path('category/<int:pk>', blog_category_view, name='blog_category_view'),
    path('search/', search_view, name='search_view'),
]
