from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .models import Order
from .forms import OrderForm
from bookings.models import Booking

import stripe
import json


@login_required
@require_POST
def cache_checkout_data(request):
    """
    Store booking info into the Stripe PaymentIntent metadata
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY

        stripe.PaymentIntent.modify(pid, metadata={
            'booking_id': request.POST.get('booking_id'),
            'save_info': request.POST.get('save_info'),
            'username': request.user.username,
        })

        return HttpResponse(status=200)
    
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be' \
            'processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)
    

def checkout(request):
    """
    Checkout page for single booking
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY