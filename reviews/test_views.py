from decimal import Decimal
from datetime import date, timedelta

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from listings.models import Property, Destination
from bookings.models import Booking
from reviews.models import Review


class AddReviewViewTests(TestCase):
    """
    Test Review view
    """

    def setUp(self):

        self.user = User.objects.create_user(
            username="bob",
            password="pass123",
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

        self.url = reverse("add_review", args=[self.property.id])

    # -------------------------
    #  Login required
    # -------------------------
    def test_add_review_requires_login(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    
    # -------------------------
    #  User without booking blocked
    # -------------------------
    def test_management_non_staff_redirects_home(self):

        logged_in = self.client.login(username="bob", password="pass123")
        self.assertTrue(logged_in)

        response = self.client.get(self.url)

        self.assertRedirects(
            response,
            reverse("property_detail", kwargs={"pk": self.property.id})
        )

    # -------------------------
    #  User with paid booking can access
    # -------------------------

    def test_user_with_paid_booking_can_view_form(self):
        Booking.objects.create(
            property=self.property,
            user=self.user,
            check_in=date.today() + timedelta(days=1),
            check_out=date.today() + timedelta(days=3),
            is_paid=True,
        )

        self.client.login(username="bob", password="pass123")
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "form")

    # -------------------------
    #  Valid POST create review
    # -------------------------

    def test_user_with_paid_booking_can_view_form(self):
        Booking.objects.create(
            property=self.property,
            user=self.user,
            check_in=date.today() + timedelta(days=1),
            check_out=date.today() + timedelta(days=3),
            is_paid=True,
        )

        self.client.login(username="bob", password="pass123")

        response = self.client.post(self.url, {
            "rating": 1,
            "comment": "test comment"
        })

        self.assertEqual(Review.objects.count(), 1)
        self.assertRedirects(
            response,
            reverse("property_detail", args=[self.property.id])
        )
