from datetime import date, timedelta
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from listings.models import Property, Destination
from bookings.models import Booking


class BookingViewTests(TestCase):

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

        self.url = reverse("create_booking", args=[self.property.id])

    def test_booking_page_loads(self):
        """
        Test if booking page loads
        """
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bookings/booking.html")

    def test_booking_post_creates_booking(self):
        """
        Test booking create
        """
        post_data = {
            "check_in": date.today() + timedelta(days=1),
            "check_out": date.today() + timedelta(days=3),
            "guests": 2,
        }

        response = self.client.post(self.url, post_data)

        self.assertEqual(Booking.objects.count(), 1)

        booking = Booking.objects.first()
        self.assertEqual(booking.user, self.user)
        self.assertEqual(booking.property, self.property)
        self.assertFalse(booking.is_paid)

        self.assertRedirects(
            response,
            reverse("checkout", args=[booking.id])
        )
