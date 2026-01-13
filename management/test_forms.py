from django.test import TestCase
from django.utils import timezone
from datetime import timedelta

from management.forms import *
from listings.models import Property


class UserFormTest(TestCase):
    def test_user_form_is_valid(self):
        """
        Test user form is valid
        """

        form = UserForm(data={
            "username": "John_Doe" ,
            "email" : "test@example.com",
            "first_name" : "John",
            "last_name" : "Doe",
            "is_staff" : False,
        })

        self.assertTrue(form.is_valid(), form.errors)

    def test_user_form_is_invalid(self):
        """
        Test user form is invalid
        """
        form = UserForm(data={})
        self.assertFalse(form.is_valid())


class BookingFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="john",
            password="password123"
        )

        self.property = Property.objects.create(
            property_name="Test Property",
            price_per_night=100
        )

    def test_booking_form_is_valid(self):
        """
        Test booking form is valid
        """
        form = BookingForm(data={
            "property" : self.property.id,
            "user" : self.user.id,
            "check_in": timezone.now().date(),
            "check_out": (timezone.now() + timedelta(days=1)).date(),
            "guests" : "1",
            "total_price" : 200,
        })

        self.assertTrue(form.is_valid(), form.errors)
