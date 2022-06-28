from .views import RouteList,BusList, TicketDetailView, TicketCreationView, ProfileView
from django.urls import path

urlpatterns = [
    path('routes/',RouteList.as_view()),
    path('buses/',BusList.as_view()),
    path('user/myticket/',TicketDetailView.as_view()),
    path('user/myticket/create/',TicketCreationView.as_view()),
    path('user/profile/',ProfileView.as_view())

]
