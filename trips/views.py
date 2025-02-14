# في ملف trips/views.py

from django.shortcuts import render, get_object_or_404
from .models import Trip
#######################################################################################
# trips/views.py

#######################################################################################

def index(request):
    trips = Trip.objects.all().order_by('-date') # أحدث 3 رحلات للصفحة الرئيسية
    return render(request,'trips/home.html', {'trips':trips})

def trips_list(request):
    all_trips = Trip.objects.all().order_by('-date')
    return render(request,'trips/trips1.html', {'all_trips': all_trips})

def trip_form(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)  # جلب بيانات الرحلة
    return render(request, 'trips/form_page.html', {'trip': trip})

    # return render(request, 'trips/form_page.html', {'trip_id': trip_id})
###########################################################################################
# def book_trip(request, trip_id):
#     trip = Trip.objects.get(id=trip_id)
    
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             booking = form.save(commit=False)
#             booking.trip = trip  # ربط الحجز بالرحلة
#             booking.save()
#             return redirect('booking_success')  # توجيه إلى صفحة النجاح
#     else:
#         form = BookingForm()
    
#     return render(request, 'trips/form_page.html', {
#         'form': form,
#         'trip': trip
#     })
# def booking_success(request):
#     return render(request, 'trips/booking_success.html')











# def submit_booking(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         trip_datetime = request.POST.get('trip_datetime')
#         # حفظ البيانات في قاعدة البيانات
#         UserInput.objects.create(
#             name=name,
#             email=email,
#             phone=phone,
#             address=address,
#             trip_datetime=trip_datetime
#         )
#         # return HttpResponse("تم حفظ البيانات بنجاح!")
    
#     return render(request, "")
