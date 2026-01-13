from decimal import Decimal
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date, timedelta

from listings.models import Property, Destination
from bookings.models import Booking
from reviews.models import Review


class ManagementDashboardTests(TestCase):

    def setUp(self):

        self.staff_user = User.objects.create_user(
            username="admin",
            password="pass123",
            is_staff=True
        )

        self.normal_user = User.objects.create_user(
            username="user",
            password="pass123",
            is_staff=False
        )

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
            user=self.staff_user,
            check_in=date.today() + timedelta(days=1),
            check_out=date.today() + timedelta(days=3),
            guests=2,
            is_paid=True,
        )

        self.review = Review.objects.create(
            booking=self.booking,
            rating=5,
            comment="Nice place"
        )

        self.url = reverse("management")

    # -------------------------
    #  Login required
    # -------------------------
    def test_management_requires_login(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    # -------------------------
    #  Non-staff redirected
    # -------------------------
    def test_management_non_staff_redirects_home(self):
        self.client.login(username="user", password="pass123")
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse("home"))

    # -------------------------
    #  Staff can access
    # -------------------------
    def test_management_staff_access_allowed(self):
        self.client.login(username="admin", password="pass123")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
