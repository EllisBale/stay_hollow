from django.contrib import admin
from .models import Property, PropertyImage, Amenity


class PropertyImage(admin.TabularInline):
    model = PropertyImage
    extra = 1


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImage]
    list_display = ("property_name", "location", "price_per_night", "guests", "is_featured", "created_at")
    list_filter = ("is_featured", "location")
    search_fields = ("property_name", "location")


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    search_fields = ("name",)
