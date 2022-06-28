from urllib import request
from rest_framework import generics
from .models import Bus,Ticket,Route
from .serializers import BusSerializer,TicketSerializer,RouteSerializer
from .permissions import IsOwner

# Create your views here.
class RouteList(generics.ListAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer




class BusList(generics.ListAPIView):
    permission_classes = IsOwner
    queryset = Bus.objects.all()
    serializer_class = BusSerializer