from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):

    guests = forms.IntegerField(
        min_value=1,
    )

    class Meta:
        model = Booking
        fields = [
            "check_in", "check_out", "guests"
        ]

        widgets = {
            "check_in": forms.DateTimeInput(attrs={"type": "date"}),
            "check_out": forms.DateTimeInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        property_obj = kwargs.pop("property_obj")
        super().__init__(*args, **kwargs)

        self.fields["guests"].widget.attrs["max"] = property_obj.guests
