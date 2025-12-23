from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .models import Order
from .forms import OrderForm
from bookings.models import Booking

import stripe


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
    

@login_required
def checkout(request, booking_id):
    """
    Checkout page for single booking
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    booking = get_object_or_404(Booking, pk=booking_id)


    # Handles form submission (POST)
    if request.method == "POST":

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            pid = request.POST.get('client_secret').split('_secret')[0]
            order = order_form.save(commit=False)
            order.order_total = booking.total_price
            order.stripe_payment_intent = pid
            order.booking = booking
            order.original_booking = booking.id
            order.user = request.user

            order.save()

            return redirect(reverse(
                'checkout_success', args=[order.order_number]
            ))
        
        else:
            messages.error(request, "There was an error with form.")


    else:
        # Handles GET request
        if not stripe_public_key:
            messages.warning(
                request, 'Stripe public key is missing.'
            )

        stripe.api_key = stripe_secret_key

        intent = stripe.PaymentIntent.create(
            amount=int(booking.total_price * 100),
            currency=settings.STRIPE_CURRENCY,
            metadata={
                "booking_id": booking.id,
                "username": request.user.username,
            }
        )

        order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'booking': booking,
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        "client_secret": intent.client_secret,
    }

    return render(request, template, context)


@login_required
def checkout_success(request, order_number):
    order = get_object_or_404(
        Order,
        order_number=order_number,
        user=request.user
        )
    
    booking = order.booking
    booking.is_paid = True
    booking.save()

    return render(request, 'checkout/checkout_success.html', {
        'order': order,
        'booking': booking
    })
