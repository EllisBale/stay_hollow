from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import Booking
from .forms import BookingForm
from listings.models import Property


@login_required
def create_booking(request, property_id):
    property_obj = get_object_or_404(Property, pk=property_id)

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.property = property_obj
            booking.is_paid = False

            try:
                booking.save()
                return redirect("checkout", booking_id=booking.id)

            except ValidationError as e:
                messages.error(request, "This date has already been booked.")

    else:
        form = BookingForm()

    return render(request, "bookings/booking.html", {
        "form": form,
        "property": property_obj,
    })



@login_required
def booking_success(request):
    return render(request, "bookings/booking_success.html")
