from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "booking",
        "property_name",
        "rating", 
        "created_at",
    )
    list_filter = (
        "rating",
        "created_at",
        "booking__property",
    )
    search_fields = (
        "booking__property__property_name",
        "user__username",
        "comment",                 
    )
    readonly_fields = (
        "created_at",
    )

    def property_name(self, obj):
        return obj.booking.property.property_name
    property_name.admin_order_field = "booking__property__property_name"
    property_name.short_description = "Property"
