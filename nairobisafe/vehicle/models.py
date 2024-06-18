# vehicles/models.py

from django.db import models

class Vehicle(models.Model):
    type = models.CharField(max_length=50)
    capacity = models.CharField(max_length=50)
    price_per_km = models.DecimalField(max_digits=10, decimal_places=2)
    plate_number = models.CharField(max_length=20, unique=True)
    brand = models.CharField(max_length=50)
    model_year = models.IntegerField()

    def __str__(self):
        return f"{self.type} - {self.plate_number}"
