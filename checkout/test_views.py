from decimal import Decimal
from datetime import date, timedelta
from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from bookings.models import Booking
from listings.models import Property, Destination


@patch("checkout.views.stripe.PaymentIntent.create")
class CheckoutViewTests(TestCase):
    """
    Test for checkout page views.
    """
    def setUp(self):

        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )
        self.client.login(username="testuser", password="password123")

        self.destination = Destination.objects.create(
            name="Test Destination",
            slug="test-destination"
        )

        self.property = Property.objects.create(
            property_name="Test Property",
            destinations=self.destination,
            price_per_night=Decimal("100.00"),
            bedrooms=2,
            guests=4,
        )

        self.booking = Booking.objects.create(
            property=self.property,
            user=self.user,
            check_in=date.today() + timedelta(days=1),
            check_out=date.today() + timedelta(days=3),
            guests=2,
            is_paid=False,
            total_price=Decimal("200.00"),
        )

        self.url = reverse("checkout", args=[self.booking.id])

    def test_checkout_page_status_200(self, mock_stripe_create):
        """
        Checkout page should load successfully for logged-in user.
        """

        mock_stripe_create.return_value.client_secret = "test_secret_123"

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout/checkout.html")
