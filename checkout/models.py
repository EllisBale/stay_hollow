from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
import uuid


class Order(models.Model):
    """
    Stores order an payment details for a property booking.
    """
    order_number = models.CharField(
        max_length=32,
        null=False,
        editable=False,
        unique=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    booking = models.OneToOneField(
        "bookings.Booking",
        on_delete=models.CASCADE,
        related_name="order"
    )

    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)

    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(
        blank_label='Country *', null=False, blank=False)

    county = models.CharField(max_length=80, null=True, blank=True)

    order_total = models.DecimalField(max_digits=10, decimal_places=2)

    stripe_payment_intent = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]

    def _generate_order_number(self):
        """
        Generates a random, unique order number UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the orignal save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {
            self.order_number} for {self.booking.property.property_name}"
