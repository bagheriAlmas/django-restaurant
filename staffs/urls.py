from django.urls import path
from .views import staff_list_view

urlpatterns = [
    path('staffs/', staff_list_view, name='staff_list_view')
]
