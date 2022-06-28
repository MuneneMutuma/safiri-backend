from django.db import models
from django.contrib.auth.models import User


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


    # def __str__(self):
    #     return f'{self.start_point} - {self.end_point}'

    def __iter__(self):
        fields = [f.name for f in self._meta.fields]
        for field in fields:
            value = getattr(self, field, None)
            yield({field: value})

class Bus(models.Model):
    number_plate = models.CharField(max_length=8, blank=False)
    BUS_ROUTE = models.ForeignKey(to =Route,on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.number_plate


class Ticket(models.Model):
    date_paid = models.DateField()
    time_paid = models.TimeField()
    seat_number = models.IntegerField()
    traveller = models.ForeignKey('users.Member', on_delete=models.CASCADE)
    payment_id = models.TextField()
    ROUTE_ID = models.ForeignKey(to=Route, on_delete=models.CASCADE)
    BUS_ID = models.ForeignKey(to=Bus,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.traveller.username)

    # def __iter__(self):
    #     fields = [f.name for f in self._meta.fields]
    #     for field in fields:
    #         value = getattr(self, field, None)
    #         yield({field: value})