from django.db import models

# Create your models here.
class Cars(models.Model):
    user_name = models.CharField(max_length=150)
    license_plate = models.CharField(max_length=100)
    car_brand = models.CharField(max_length=100)
    car_year = models.IntegerField()
    car_color = models.CharField(max_length=100)
    RENAVAM = models.IntegerField()

