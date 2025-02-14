# في ملف trips/admin.py
from django.contrib import admin
from .models import Trip
# from .models import Booking



@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'date', 'capacity')
    search_fields = ('title', 'description')
    list_filter = ('date',)


# @admin.register(Booking)
# class BookingAdmin(admin.ModelAdmin):
#     list_display = ('user_name', 'trip', 'booking_date')
#     list_filter = ('trip',)
#     search_fields = ('user_name', 'email', 'trip__title')