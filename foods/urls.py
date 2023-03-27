from django.urls import path
from .views import special_food_list, food_detail,menu_list

urlpatterns = [
    path('', special_food_list, name='foods'),
    path('foods/<int:pk>', food_detail, name='food_detail'),
    path('foods/menu/', menu_list, name='menu'),
]
