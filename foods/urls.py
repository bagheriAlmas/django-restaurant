from django.urls import path
from .views import special_food_list_view, food_detail_view, menu_list_view, gallery_list_view

urlpatterns = [
    path('', special_food_list_view, name='foods'),
    path('foods/<int:pk>', food_detail_view, name='food_detail'),
    path('foods/menu/', menu_list_view, name='menu'),
    path('foods/gallery/', gallery_list_view, name='gallery'),
]
