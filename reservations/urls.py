from django.urls import path
from .views import reserve_view,contact_us_view

urlpatterns = [
    path('reservations/', reserve_view, name='reserve_view'),
    path('contact-us/', reserve_view, name='contact_us'),
]
