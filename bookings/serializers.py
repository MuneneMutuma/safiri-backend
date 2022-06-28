
from rest_framework import serializers
from .models import  Route
from .models import Ticket
from .models import Bus


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
       fields = ('id','date_paid','seat_number','traveller','payment_id','time_paid','BUS_ID','ROUTE_ID')
       model = Ticket
       
    
class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','start_point','end_point','departure_time','price')
        model = Route
    
class BusSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','number_plate','BUS_ROUTE')
        model = Bus