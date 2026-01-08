from decimal import Decimal
from django.test import TestCase
from django.contrib.auth.models import User

from checkout.models import Order
from bookings.models import Booking
from listings.models import Property, Destination


class OrderModelTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="testuser",
            password="pass123"
        )

        self.destination = Destination.objects.create(
            name="Beach",
            slug="beach"
        )

        self.property = Property.objects.create(
            property_name="Sea View Apartment",
            destinations=self.destination,
            price_per_night=Decimal("120.00"),
            bedrooms=2,
            guests=4,
        )

        self.booking = Booking.objects.create(
            user=self.user,
            property=self.property,
            check_in="2026-01-10",
            check_out="2026-01-15",
            total_price=Decimal("600.00"),
            is_paid=False,
        )

        self.order = Order.objects.create(
            user=self.user,
            booking=self.booking,
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            phone_number="123456789",
            town_or_city="London",
            street_address1="123 Main Street",
            postcode="D01XYZ",
            country="IE",
            order_total=Decimal("600.00"),
            stripe_payment_intent="pi_test_123",
        )


    # --------------------
    # Uniqueness Test
    # --------------------
    def test_order_number_is_unique(self):
        order2 = Order.objects.create(
            user=self.user,
            booking=Booking.objects.create(
                user=self.user,
                property=self.property,
                check_in="2026-02-01",
                check_out="2026-02-05",
                total_price=Decimal("480.00"),
                is_paid=False,
            ),
            first_name="Jane",
            last_name="Smith",
            email="jane@example.com",
            phone_number="987654321",
            town_or_city="Cork",
            street_address1="456 Side Street",
            postcode="T12ABC",
            country="IE",
            order_total=Decimal("480.00"),
        )

        self.assertNotEqual(
            self.order.order_number,
            order2.order_number
        )
