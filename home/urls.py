# # home/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home_view, name='home'),
# ]
###############################################

# home/urls.py (أنشئ الملف)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
]