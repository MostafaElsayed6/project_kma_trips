from django import forms
from .models import Trip
# from .models import Booking

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['title', 'description', 'image', 'capacity']

# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ['user_name', 'email', 'phone', 'address', 'booking_date']
#         widgets = {
#             'booking_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#         }