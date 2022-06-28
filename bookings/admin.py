from django.contrib import admin
from .models import Bus, Route, Ticket

# Register your models here.
admin.site.register(Bus)
admin.site.register(Route)
admin.site.register(Ticket)
