from django.contrib import admin
from .models import Property, PropertyImage


class PropertyImage(admin.TabularInline):
    model = PropertyImage
    extra = 1


@admin.register(Property)
class Property