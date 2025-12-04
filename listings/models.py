from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


class Amenity(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name



class Destination(models.Model):
    name = models.CharField(max_length=100, unique=True)

    parent_destination = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="sub_destinations"
    )

    slug = models.SlugField(max_length=120, unique=True)

    class Meta:
        verbose_name_plural = "Destinations"

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Property(models.Model):
    property_name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)

    destinations = models.ForeignKey(
        Destination,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="properties"
    )

    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    guests = models.PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ]
    )
    
    main_image = CloudinaryField(
        "image",
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
    image = CloudinaryField(
        "image",
        folder="property_images")

    def __str__(self):
        return f"Extra Image for {self.property.property_name}"



