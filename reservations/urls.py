from django.urls import path
from .views import reserve_view

urlpatterns = [
    path('reservations/', reserve_view, name='reserve_view')
]
