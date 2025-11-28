from django.http import HttpResponse
from bookings.models import Booking

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id

        # Metadata
        booking_id = intent.metadata.get("booking_id")
        save_info = intent.metadata.get("save_info")

        if not booking_id:
            return HttpResponse(
                content="Webhook Error: No booking ID in metadata",
                status=400
            )

        # Retry loop (same structure as original example)
        booking_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                booking = Booking.objects.get(id=booking_id)
                booking_exists = True
                break
            except Booking.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if booking_exists:
            # Mark booking as paid
            booking.is_paid = True
            booking.stripe_pid = pid
            booking.save()

            return HttpResponse(
                content=(f'Webhook received: {event["type"]} | SUCCESS: '
                         f'Booking {booking_id} marked as paid'),
                status=200
            )

        else:
            return HttpResponse(
                content=(f'Webhook received: {event["type"]} | ERROR: '
                         f'Booking {booking_id} not found after retries'),
                status=404
            )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )