from bookings.models import Route, Bus, Ticket
from rest_framework import serializers

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['start_point', 'end_point', 'departure_time', 'date', 'price', 'BUS_ID', 'seats', 'id']
