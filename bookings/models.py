# bookings/models.py
from django.db import models
from django.contrib.auth import get_user_model
from trips.models import Trip

User = get_user_model()

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    seats = models.PositiveIntegerField()
    booked_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')  # مثل: confirmed, cancelled

    def __str__(self):
        return f"{self.user.username} - {self.trip.title}"