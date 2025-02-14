# # home/views.py
# from django.shortcuts import render

# def home_view(request):
#     return render(request, 'home.html')



# home/views.py
from django.shortcuts import render
from trips.models import Trip  # استيراد نموذج الرحلات

def home_page(request):
    featured_trips = Trip.objects.all()[:3]  # عرض 3 رحلات مميزة
    return render(request, 'home/index.html', {'featured_trips': featured_trips})