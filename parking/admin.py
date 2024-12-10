from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Location, ParkingSpace, Booking

admin.site.register(Location)
admin.site.register(ParkingSpace)
admin.site.register(Booking)
