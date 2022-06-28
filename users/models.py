from django.db import models
from django.contrib.auth.models import AbstractUser


class Member(AbstractUser):
    date_of_birth = models.DateField(null=True,blank=False)
    phone_number = models.IntegerField(unique=True,null=True, blank=False)
    national_id = models.IntegerField(unique=True, null=True,blank=False)
