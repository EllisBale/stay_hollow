from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Booking(models.Model):
    property = models.ForeignKey(
        "listings.Property",
        on_delete=models.CASCADE,
        related_name="bookings"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookings"
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ]
    )
    total_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.CheckConstraint(
                check=models.Q(check_in__lt=models.F("check_out")),
                name="checkin_before_checkout"
            )
        ]

    def __str__(self):
        return f"{self.user.username} booking for {self.property.property_name}"


    def clean(self):
        """
        Prevents user from double bookings by checking for overlap.
        """

        if not self.property_id:
            return

        overlapping = Booking.objects.filter(
            property=self.property,
            is_paid=True,
            check_out__gt=self.check_in,
            check_in__lt=self.check_out
        )

        if self.pk:
            overlapping = overlapping.exclude(pk=self.pk)

        if overlapping.exists():
            raise ValidationError("This Property is already booked for these dates.")


    def number_of_nights(self):
        """Return total number of nights booked"""
        return (self.check_out - self.check_in).days


    def calculate_total_price(self):
        """Calculate total price based on property nightly rate"""
        return self.number_of_nights() * self.property.price_per_night


    def save(self, *args, **kwargs):

        self.full_clean()

        if not self.total_price:
            self.total_price = self.calculate_total_price()
        super().save(*args, **kwargs)
