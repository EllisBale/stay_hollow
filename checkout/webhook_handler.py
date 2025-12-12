from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order
from bookings.models import Booking

import time


class StripeWH_Handler:
    """
    Handle Stripe webhooks
    """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        if not cust_email:
            return
        
        booking = order.booking

        subject = render_to_string(
            "checkout/confirmation_emails/confirmation_email_subject.txt",
            {"order": order},
        )
        body = render_to_string(
            "checkout/confirmation_emails/confirmation_email_body.txt",
            {"order": order, "booking": booking, "contact_email": settings.DEFAULT_FROM_EMAIL},
        )

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )


    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """Handle payment success webhook"""
        intent = event.data.object
        pid = intent.id
        booking_id = intent.metadata.get("booking_id")

        if not booking_id:
            return HttpResponse(
                content="Webhook Error: No booking ID in metadata",
                status=400
            )

        booking_id = int(booking_id)

        # Retry loop for booking creation delay
        booking = None
        for _ in range(5):
            try:
                booking = Booking.objects.get(id=booking_id)
                break
            except Booking.DoesNotExist:
                time.sleep(1)

        if not booking:
            return HttpResponse(
                content=f"Webhook Error: Booking {booking_id} not found",
                status=404
            )

        # Update booking
        booking.is_paid = True
        booking.save()

        # Update matching order
        try:
            order = Order.objects.get(booking_id=booking_id)
            order.stripe_payment_intent = pid
            order.save()

            self._send_confirmation_email(order)

        except Order.DoesNotExist:
            pass

        return HttpResponse(
            content=f"Webhook received: {event['type']} | SUCCESS",
            status=200
        )


    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )