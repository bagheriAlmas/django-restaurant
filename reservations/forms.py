from django import forms
from .models import Reservation,ContactUs


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
