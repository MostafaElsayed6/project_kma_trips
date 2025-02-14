# bookings/admin.py
from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'trip', 'seats', 'booked_at', 'status')
    list_filter = ('status',)