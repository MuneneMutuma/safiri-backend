from django.urls import path
from bookings import views as bk_views

urlpatterns = [
    path('', bk_views.GetRoutes.as_view()),
    path('getroute/<int:pk>', bk_views.GetRoute.as_view()),
    path('post/', bk_views.GetRouteBySearch.as_view()),
]