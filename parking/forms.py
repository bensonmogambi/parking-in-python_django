from django import forms
from .models import Booking
from django.utils import timezone

class BookingForm(forms.ModelForm):
    start_time = forms.DateTimeField(initial=timezone.now)
    end_time = forms.DateTimeField(initial=timezone.now)

    class Meta:
        model = Booking
        fields = ['user_name', 'start_time', 'end_time']
