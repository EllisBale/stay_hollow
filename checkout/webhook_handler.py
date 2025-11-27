from django.http import HttpResponse
from bookings.models import Booking
import stripe


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Fallback for any event not specifically handled"""
        return HttpResponse(
            content=f"Unhandled event type: {event['type']}",
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """Handle successful payment"""
        intent = event.data.object
        pid = intent.id
        # Read the booking ID from metadata
        booking_id = intent.metadata.get("booking_id")
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details


        if not booking_id:
            return HttpResponse(
                content="No booking ID in metadata",
                status=400,
            )

        try:
            booking = Booking.objects.get(id=booking_id)
            booking.is_paid = True
            booking.save()
        except Booking.DoesNotExist:
            return HttpResponse(
                content="Booking not found",
                status=404
            )

        return HttpResponse(
            content="Payment confirmed and booking marked as paid",
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """Handle failed payment"""
        return HttpResponse(
            content=f"Payment failed event: {event['type']}",
            status=200
        )