from django.contrib import admin
from .models import Event, Location

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("start_date", "end_date", "expense")

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "street", "zip_code", "capacity")


    # FIX HERE #