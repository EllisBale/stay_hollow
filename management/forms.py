from django import forms
from django.contrib.auth.models import User
from bookings.models import Booking
from reviews.models import Review

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "is_staff"
        ]

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "property",
            "user",
            "check_in",
            "check_out",
            "guests",
            "total_price",
        ]


