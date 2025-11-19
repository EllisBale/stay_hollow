from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "check_in", "check_out", "guests"
        ]

        widgets = {
            "check_in": forms.DateTimeInput(attrs={"type": "date"}),
            "check_out": forms.DateTimeInput(attrs={"type": "date"}),
            "guests": forms.NumberInput(attrs={"min": 1, "max": 10}),
        }