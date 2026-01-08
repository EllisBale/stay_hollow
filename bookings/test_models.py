from datetime import date, timedelta
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from bookings.models import Booking
from listings.models import Property, Destination


class BookingModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="password"
        )

        self.destination = Destination.objects.create(
            name="Beach",
            slug="beach"
        )

        self.property = Property.objects.create(
            property_name="Beach House",
            destinations=self.destination,
            price_per_night=Decimal("100.00"),
            bedrooms=2,
            guests=4,
        )

        self.check_in = date.today() + timedelta(days=5)
        self.check_out = self.check_in + timedelta(days=3)

        self.booking = Booking.objects.create(
            user=self.user,
            property=self.property,
            check_in=self.check_in,
            check_out=self.check_out,
            guests=2,
        )

    def test_prevents_overlapping_paid_bookings(self):
        self.booking.is_paid = True
        self.booking.save()

        overlapping_booking = Booking(
            user=self.user,
            property=self.property,
            check_in=self.check_in + timedelta(days=1),
            check_out=self.check_out + timedelta(days=1),
            guests=1,
        )

        with self.assertRaises(ValidationError):
            overlapping_booking.save()
