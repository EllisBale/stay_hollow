from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from bookings.models import Booking


def checkout(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
