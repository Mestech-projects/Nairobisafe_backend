from django.db import models

class Service(models.Model):
    SERVICE_CHOICES = [
        ('Packaging', 'Packaging'),
        ('Cleaning', 'Cleaning'),
    ]
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.service_type
