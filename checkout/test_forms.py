from django.test import TestCase
from checkout.forms import OrderForm


class OrderFormTest(TestCase):

    def test_order_form_is_valid(self):
        """
        Valid form test
        """
        form = OrderForm(data={
            "first_name": "John",
            "last_name": "Doe",
            "email": "test@example.com",
            "phone_number": "07123456789",
            "postcode": "TE5 5As",
            "town_or_city": "London",
            "street_address1": "Street 1",
            "street_address2":  "Street 2",
            "country": "GB",
            "county": "London",
        })

        self.assertTrue(form.is_valid(), form.errors)

    def test_order_form_is_invalid(self):
        """
        Test if form is invalid
        """
        form = OrderForm(data={})
        self.assertFalse(form.is_valid())
