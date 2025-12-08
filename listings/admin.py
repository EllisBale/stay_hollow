from django.contrib import admin
from django.utils.html import format_html
from .models import Destination, Property, PropertyImage, Amenity


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ("name", "parent_destination", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)
    list_filter = ("parent_destination",)

class PropertyImage(admin.TabularInline):
    model = PropertyImage
    extra = 1


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImage]
    list_display = ("property_name", "price_per_night", "guests", "bedrooms", "is_featured", "created_at")
    list_filter = ("is_featured",)
    search_fields = ("property_name",)


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ("name", "icon_preview")

    def icon_preview(self, obj):
        if obj.icon_class:
            return format_html("<i class='{}'></i>", obj.icon_class)
        return "-"
    icon_preview.short_description = "Icon"