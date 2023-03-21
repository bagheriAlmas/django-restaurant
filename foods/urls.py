from django.urls import path
from .views import food_list, food_detail

urlpatterns = [
    path('foods/', food_list, name='foods'),
    path('foods/<int:pk>', food_detail, name='food_detail'),
]
