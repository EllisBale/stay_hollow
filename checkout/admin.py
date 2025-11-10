from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_number", "user", "booking", "order_total", "date")
    search_fields = ("order_number", "user__username", "booking__property__property_name")
    list_filter = ("date",)

