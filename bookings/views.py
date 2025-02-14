# bookings/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from trips.models import Trip
from .models import Booking

@login_required
def book_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    
    if request.method == 'POST':
        seats = int(request.POST.get('seats', 1))
        
        # التحقق من توفر الأماكن
        if seats <= trip.capacity:
            # إنشاء الحجز
            Booking.objects.create(
                user=request.user,
                trip=trip,
                seats=seats
            )
            # تحديث السعة المتبقية
            trip.capacity -= seats
            trip.save()
            return redirect('booking_confirmation')
        else:
            # عرض خطأ إذا لم تكن الأماكن كافية
            return render(request, 'bookings/error.html', {'error': 'لا توجد أماكن كافية'})
    
    return render(request, 'bookings/book.html', {'trip': trip})

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/list.html', {'bookings': bookings})

def booking_confirmation(request):
    return render(request, 'bookings/confirmation.html')