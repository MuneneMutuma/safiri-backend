from bookings.models import Route
from rest_framework.views import APIView
from rest_framework.response import Response
from bookings.serializers import RouteSerializer
import json

class GetRoutes(APIView):
    """
    Lists all the routes availible
    """
    def get(self, request):
        routes = Route.objects.all()
        serializer = RouteSerializer(routes, many=True)
        formatted_response = list()
        for item in serializer.data:
            obj = {
                "from": item["start_point"],
                "to": item["end_point"],
                "time": item["departure_time"],
                "date": item["date"],
                "price": item["price"],
                "carId": item["BUS_ID"],
                "routeId": item["id"]
            }
            formatted_response.append(json.dumps(obj))
        return Response(formatted_response)

class GetRoute(APIView):
    """
    gets a specific route
    """
    def get(self, request, pk):
        route = Route.objects.get(pk=pk)
        serializer = RouteSerializer(route)
        seats = serializer.data['seats']
        formatted_response = list()
        for seat in seats.keys():
            tmp = dict()
            tmp["seatNo"] = seat
            tmp["taken"] = int(seats[seat] == "T")
            formatted_response.append(tmp)

        return Response(formatted_response)



class GetRouteBySearch(APIView):
    def post(self, request):
        data = request.data
        routes = Route.objects.filter(
            start_point = data['from'],
            end_point = data['to'],
            date = data['date'],
        )
        serializer = RouteSerializer(routes, many=True)
        formatted_response = list()
        for item in serializer.data:
            tmp = dict()
            tmp = {
                "from": item["start_point"],
                "to": item["end_point"],
                "time": item["departure_time"],
                "date": item["date"],
                "price": item["price"],
                "carId": item["BUS_ID"],
                "routeId": item["id"]
            }
            print(tmp)
            formatted_response.append(json.dumps(tmp))
        print(formatted_response)
        return Response(formatted_response)
