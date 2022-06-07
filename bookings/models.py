from django.db import models
from users.models import Msafiri


class Bus(models.Model):
    number_plate = models.CharField(max_length=8, blank=False)

class Route(models.Model):
    PLACES_CHOICES = (
    ("NRB", "Nairobi"),
    ("ELD", "Eldoret"),
    ("NAK", "Nakuru"),
    ("NAV", "Naivasha"),
    ("NYR", "Nyeri"),
    ("NYH", "Nyahururu"),
    ("KIT", "Kitale"),
    ("MAK", "Makueni"),
    ("JUJ", "Juja"),
    ("THK", "Thika")
    )

    start_point = models.CharField(
        max_length=3,
        choices=PLACES_CHOICES,
        default=None,
        blank=False,
    )
    end_point = models.CharField(
        max_length=3,
        choices=PLACES_CHOICES,
        default=None,
        blank=False,
    )
    departure_time = models.TimeField(blank=False)
    price = models.IntegerField()
    date = models.DateField()
    seats = models.JSONField()
    BUS_ID = models.ForeignKey(to=Bus, on_delete=models.CASCADE)

class Ticket(models.Model):
    date_paid = models.DateField()
    time_paid = models.TimeField()
    seat_number = models.IntegerField()
    traveller = models.ForeignKey(to=Msafiri, on_delete=models.CASCADE)
    payment_id = models.TextField()
    ROUTE_ID = models.ForeignKey(to=Route, on_delete=models.CASCADE)