
from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100, default='Nairobi')

    def __str__(self):
        return f"{self.name} - {self.city}"

class ParkingSpace(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    slot_number = models.CharField(max_length=50)
    available = models.BooleanField(default=True)  # True if the space is available for booking
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Slot {self.slot_number} at {self.location.name} - {('Available' if self.available else 'Booked')}"

class Booking(models.Model):
    user_name = models.CharField(max_length=100)
    parking_space = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.user_name} at {self.parking_space.location.name} from {self.start_time} to {self.end_time}"
