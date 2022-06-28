from requests import Response
from bookings.permissions import IsOwner
from bookings.models import Ticket,Bus,Route
from users.models import Member
from bookings.serializers import RouteSerializer,TicketSerializer,BusSerializer
from users.serializers import MemberSerializer
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.

#get a list of routes
class RouteList(generics.ListAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

#get list of buses
class BusList(generics.ListAPIView):
    serializer_class = BusSerializer

    def get_queryset(self):
        return Bus.objects.all()
    

#get your ticket
class TicketDetailView(generics.ListAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        user = self.request.user
        return Ticket.objects.filter(traveller = user.id)
    
    def get(self, request):
        user = self.request.user
        tickets = user.ticket_set.all()
        ticket_list = list()
        ticket_details = dict()
        fields = ["date_paid", "time_paid", "seat_number", "payment_id"]

        for ticket in tickets:
            route = ticket.ROUTE_ID
            route_details = dict()

            for item in route:
                route_details.update(item)
            
            ticket_details.update(route_details)

            for field in fields:
                ticket_details[field] = ticket.__dict__[field]
            ticket_list.append(ticket_details)
        return Response(ticket_list)


#create your ticket
class  TicketCreationView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        user = self.request.user
        return Ticket.objects.filter(traveller = user)

#get your profile
class ProfileView(generics.ListAPIView):
    serializer_class = MemberSerializer

    def get_queryset(self):
        user = self.request.user
        return Member.objects.filter(username = user.username)
    
