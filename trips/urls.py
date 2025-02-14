# في ملف trips/urls.py
from django.urls import path
from . import views 
# from .views import save_to_database




# urlpatterns = [
#     path('', views.trip_list, name='trip_list'),
#     path('<int:trip_id>/', views.trip_detail, name='trip_detail'),
# ]

from trips import views

urlpatterns = [
    path('', views.index, name='Trip'),
    # path('x/', views.trips_list, name='trips_list'),
    path('trips/', views.trips_list, name='trips_list'), # صفحة قائمة الرحلات
    # path('trip_detail/', views.trip_form, name='trip_detail')
    path('trip/<int:trip_id>/', views.trip_form, name='trip_form'),  # تأكد من وجود هذا السطر
    # path('save/', save_to_database, name='save_to_database'),
    # path('book/<int:trip_id>/', views.book_trip, name='book_trip'),
    # path('booking-success/', views.booking_success, name='booking_success'),
]