from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestOrderHistoryViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )
        self.client.login(username="testuser", password="password123")

    def test_order_history_page(self):
        """
        Test if order history Page returns status code 200.
        """
        response = self.client.get(reverse("order_history"))
        self.assertEqual(response.status_code, 200)
