from django.urls import path
from .views import blog_list_view, blog_detail_view

urlpatterns = [
    path('blogs/', blog_list_view, name='blog_list_view'),
    path('blogs/<int:pk>', blog_detail_view, name='blog_detail_view'),
]