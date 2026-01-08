from decimal import Decimal
from django.test import TestCase
from listings.models import Amenity, Destination, Property, PropertyImage


class AmenityModelTest(TestCase):

    def test_string_representation(self):
        amenity = Amenity.objects.create(
            name="WiFi",
            icon_class="fa-wifi"
        )
        self.assertEqual(str(amenity), "WiFi")


class DestinationModelTest(TestCase):

    def test_destination_slug_is_auto_created(self):
        destination = Destination.objects.create(
            name="England",
            slug=""
        )
        self.assertEqual(destination.slug, "ocean-view")

    def test_string_representation(self):
        destination = Destination.objects.create(
            name="England",
            slug="engalnd"
        )
        self.assertEqual(str(destination), "Beach")


class PropertyModelTest(TestCase):

    def setUp(self):
        self.destination = Destination.objects.create(
            name="Mountains",
            slug="mountains"
        )

        self.property = Property.objects.create(
            property_name="Luxury Cabin",
            destinations=self.destination,
            price_per_night=Decimal("150.00"),
            bedrooms=3,
            guests=6,
            latitude=Decimal("53.123456"),
            longitude=Decimal("-6.123456"),
        )

    def test_property_created(self):
        self.assertEqual(Property.objects.count(), 1)

    def test_string_representation(self):
        self.assertEqual(str(self.property), "Luxury Cabin")

    def test_formatted_price(self):
        self.assertEqual(self.property.formatted_price(), "150")

    def test_maps_url(self):
        url = self.property.maps_url()
        self.assertIn("google.com/maps", url)
        self.assertIn("53.123456", url)
        self.assertIn("-6.123456", url)

    def test_property_has_destination(self):
        self.assertEqual(self.property.destinations.name, "Mountains")
