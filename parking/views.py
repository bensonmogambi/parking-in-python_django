from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Location, ParkingSpace, Booking
from django.utils import timezone
from .forms import BookingForm


def available_parking(request):
    locations = Location.objects.all()
    available_spaces = ParkingSpace.objects.filter(available=True)
    return render(request, 'parking/available_parking.html',
                  {'locations': locations, 'available_spaces': available_spaces})


def book_parking(request, space_id):
    parking_space = ParkingSpace.objects.get(id=space_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.parking_space = parking_space
            # Calculate total price
            booking.total_price = (
                                              booking.end_time - booking.start_time).total_seconds() / 3600 * parking_space.price_per_hour
            booking.save()

            # Mark the parking space as unavailable
            parking_space.available = False
            parking_space.save()

            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm()

    return render(request, 'parking/book_parking.html', {'parking_space': parking_space, 'form': form})


def booking_confirmation(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'parking/booking_confirmation.html', {'booking': booking})
