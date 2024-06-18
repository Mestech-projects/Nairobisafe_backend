from rest_framework import serializers
from .models import Order
from vehicle.serializers import VehicleSerializer
from services.serializers import ServiceSerializer
from customers.serializers import CustomerSerializer

class OrderSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)
    vehicle = VehicleSerializer(read_only=True)
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

