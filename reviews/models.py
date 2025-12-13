from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):

    booking = models.OneToOneField(
        "bookings.Booking",
        on_delete=models.CASCADE,
        related_name="review"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviews"
    )

    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.CheckConstraint(
                check=models.Q(rating__gte=1, rating__lte=5),
                name="rating_between_1_and_5"
            )
        ]

    def __str__(self):
        return f"Review by {self.user} for booking {self.booking_id}"