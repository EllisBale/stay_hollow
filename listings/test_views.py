from django.test import TestCase
from django.urls import reverse


class PropertyViewsTestCase(TestCase):
    """Tests for property listing page"""

    def test_about_page(self):
        """
        Test if listing Page returns status code 200.
        """
        response = self.client.get(reverse("properties"))
        self.assertEqual(response.status_code, 200)

