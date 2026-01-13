from django.test import TestCase
from django.utils import timezone
from datetime import timedelta

from bookings.forms import BookingForm


class BookingFormTest(TestCase):

    def test_booking_form_is_valid(self):
        """
        Test form is valid
        """
        form = BookingForm(data={
            "check_in": timezone.now().date(),
            "check_out": (timezone.now() + timedelta(days=1)).date(),
            "guests": 1,
        })

        self.assertTrue(form.is_valid())

    def test_form_missing_fields(self):
        """
        Test form is invalid
        """
        form = BookingForm(data={

        })

        self.assertFalse(form.is_valid())
        self.assertIn("check_in", form.errors)
        self.assertIn("check_out", form.errors)
        self.assertIn("guests", form.errors)
