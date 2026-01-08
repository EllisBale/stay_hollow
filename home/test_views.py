from django.test import TestCase
from django.urls import reverse


class TestHomeViews(TestCase):
    """
    Test for Home Page.
    """
    def test_home_page(self):
        """
        Test if Home Page returns status code 200.
        """
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)


class TestAboutViews(TestCase):
    """
    Test for About Page.
    """
    def test_about_page(self):
        """
        Test if About Page returns status code 200.
        """
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)


class TestContactViews(TestCase):
    """
    Test for Contact Page.
    """
    def test_contact_page(self):
        """
        Test if Contact Page returns status code 200.
        """
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
