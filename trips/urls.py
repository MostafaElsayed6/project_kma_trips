# في ملف trips/urls.py
from django.urls import path
from . import views 
# from .views import save_to_database

from trips import views

urlpatterns = [
    path('', views.index, name='Trip'),
    path('trips/', views.trips_list, name='trips_list'), # صفحة قائمة الرحلات
    path('trip/<int:trip_id>/', views.trip_form, name='trip_form'),  # تأكد من وجود هذا السطر
    
    # path('book-trip/', views.book_trip, name='book_trip'),      
]