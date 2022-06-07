from django.db import models
from django.contrib.auth.models import User

class Msafiri(models.Model):
    phone_number = models.IntegerField(unique=True, blank=False)
    name = models.CharField(max_length= 64, blank=False)
    national_id = models.IntegerField(unique=True, blank=False)


class Member(User):
    date_of_birth = models.DateField(blank=False)
    phone_number = models.IntegerField(unique=True, blank=False)
    national_id = models.IntegerField(unique=True, blank=False)