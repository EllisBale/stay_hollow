from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


class Amenity(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon_class = models.CharField(
        max_length=150,
        blank=True,
        help_text="Enter the FontAwesome icon class."
    )

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

    area_description = models.TextField(
        blank=True,
        null=True,
        help_text="Description of the area."
    )

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

    destinations = models.ForeignKey(
        Destination,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="properties"
    )

    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    bedrooms = models.PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(15),
        ]
    )
    guests = models.PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(30),
        ]
    )
    
    main_image = CloudinaryField(
        "image",
        default="placeholder",
        folder="property_images",
    )

    description = models.TextField(blank=True, null=True)
    

    latitude = models.DecimalField(
        max_digits=18,
        decimal_places=14,
        null=True,
        blank=True,
        help_text="Paste only the numeric latitude value. Right-click on Google Maps => Copy the first set of numbers and paste in here."

    )
    longitude = models.DecimalField(
        max_digits=18,
        decimal_places=14,
        null=True,
        blank=True,
        help_text="Paste only the numeric longitude value. Right-click on Google Maps => Copy the second set of numbers and paste in here."
    )

    amenities = models.ManyToManyField(Amenity, blank=True, related_name="properties")
    is_featured = models.BooleanField(default=False, help_text="Mark yes for property to be featured on Homepage")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-is_featured", "-created_at"]


    def formatted_price(self):
        """
        Return price per night and formats it 
        for templates
        """
        return f"{self.price_per_night:,.0f}"    

    def __str__(self):
        return self.property_name
    
    def maps_url(self):
        """
        Return Google Maps link based on 
        latitude and longitude
        """
        return f"https://www.google.com/maps/search/?api=1&query={self.latitude},{self.longitude}"


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="extra_images")
    image = CloudinaryField(
        "image",
        folder="property_images",
        blank=True
    )

    def __str__(self):
        return f"Extra Image for {self.property.property_name}"



