# في ملف trips/models.py
from django.db import models

class Trip(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان الرحلة")
    location = models.CharField(max_length=200, verbose_name="موقع الرحلة", default="Default Location")
    responsible_phone = models.CharField(max_length=20, verbose_name="هاتف المسؤول")
    description = models.TextField(verbose_name="الوصف")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    duration = models.CharField(max_length=50, verbose_name="المدة")  # مثال: "3 ساعات"
    capacity = models.PositiveIntegerField(verbose_name="السعة")  # عدد الأماكن المتاحة
    image = models.ImageField(upload_to='trips/', verbose_name="الصورة")
    date = models.DateTimeField(verbose_name="تاريخ الرحلة")
    def __str__(self):
        return self.title
    


# class UserInput(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField()
#     phone = models.CharField(max_length=20)
#     address = models.TextField()
#     trip_datetime = models.DateTimeField()
#     def __str__(self):
#         return self.name

# from django.db import models


# class Trip(models.Model):
#     title = models.CharField(max_length=200, verbose_name="عنوان الرحلة")
    # location = models.CharField(max_length=200, verbose_name="موقع الرحلة")  # حقل جديد
#     responsible_phone = models.CharField(max_length=20, verbose_name="هاتف المسؤول")  # حقل جديد
#     description = models.TextField(verbose_name="الوصف")
#     price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
#     duration = models.CharField(max_length=50, verbose_name="المدة")
#     capacity = models.PositiveIntegerField(verbose_name="السعة")
#     image = models.ImageField(upload_to='trips/', verbose_name="الصورة")
#     date = models.DateTimeField(verbose_name="تاريخ الرحلة")

#     def __str__(self):
#         return self.title