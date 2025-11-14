from django.db import models
from cloudinary.models import CloudinaryField


class Amenity(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Property(models.Model):
    property_name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    guests = models.PositiveIntegerField(default=1)
    main_image = CloudinaryField(
        "Main Image",
        default="placeholder",
        folder="property_images"
    )

    description = models.TextField(blank=True, null=True)

    amenities = models.ManyToManyField(Amenity, blank=True, related_name="properties")
    is_featured = models.BooleanField(default=False, help_text="Mark yes for property to be featured on Homepage")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-is_featured", "-created_at"]

    def __str__(self):
        return self.property_name


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="extra_images")
    image = CloudinaryField("Extra Image", folder="property_images")

    def __str__(self):
        return f"Extra Image for {self.property.property_name}"
