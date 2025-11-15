from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm
from listings.models import Property


@login_required
def create_booking(request, property_id):
    property_obj = get_object_or_404(Property, pk=property_id)

    form = BookingForm()  

    return render(request, "bookings/booking.html", {
        "form": form,
        "property": property_obj,
    })


