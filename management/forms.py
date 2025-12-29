from django import forms
from django.contrib.auth.models import User
from bookings.models import Booking
from listings.models import Property, PropertyImage



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

class ListingForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            "property_name",
            "destinations",
            "price_per_night",
            "bedrooms",
            "guests",
            "main_image",
            "description",
            "latitude",
            "longitude",
            "amenities",
            "is_featured",
        ]

class ImagesForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = [
            "image",

        ]

