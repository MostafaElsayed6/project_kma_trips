# bookings/urls.py
from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('book/<int:trip_id>/', views.book_trip, name='book_trip'),
    path('list/', views.booking_list, name='booking_list'),
    path('confirmation/', views.booking_confirmation, name='booking_confirmation'),
]