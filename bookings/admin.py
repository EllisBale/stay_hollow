from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "property",
        "user",
        "check_in",
        "check_out",
        "guests",
        "total_price",
        "is_paid"
    )
    list_filter = ("is_paid", "check_in", "check_out")
    search_fields = ("property__property_name", "user__username")
    readonly_fields = ("total_price",)
