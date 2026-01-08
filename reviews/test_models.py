from django.test import TestCase
from django.contrib.auth.models import User
from decimal import Decimal

from listings.models import Property, Destination
from bookings.models import Booking
from reviews.models import Review
from datetime import date, timedelta


class ReviewModelTests(TestCase):
    """
    Test Review Model
    """

    def setUp(self):

        self.user = User.objects.create_user(
            username="testuser",
            password="pass123"
        )

        self.destinations = Destination.objects.create(
            name="Test dest",
            slug="test-destination"
        )

        self.property = Property.objects.create(
            property_name="Test Property",
            destinations=self.destinations,
            price_per_night=Decimal("100.00"),
            bedrooms=2,
            guests=4,
        )

        self.booking = Booking.objects.create(
            user=self.user,
            property=self.property,
            check_in=date.today() + timedelta(days=1),
            check_out=date.today() + timedelta(days=3),
            is_paid=True,
        )


    def test_review_create(self):
        review = Review.objects.create(
            booking=self.booking,
            user=self.user,
            rating=5,
            comment="Test comment"
        )

        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.user.username, "testuser")
