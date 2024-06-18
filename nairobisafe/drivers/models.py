from django.db import models

from vehicle.models import Vehicle

class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    license_number = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='drivers')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
