

from django.db import models
from drivers.models import Driver

class Tracking(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='tracking')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tracking {self.driver} at {self.timestamp}"
