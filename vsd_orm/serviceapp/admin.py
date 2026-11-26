from django.contrib import admin
from .models import VehicleService


@admin.register(VehicleService)
class VehicleServiceAdmin(admin.ModelAdmin):
    list_display = (
        "registration_number",
        "owner_name",
        "vehicle_type",
        "brand",
        "vehicle_model",
        "service_type",
        "service_date",
        "service_cost",
        "status",
    )
    list_filter = ("vehicle_type", "service_type", "status", "service_date")
    search_fields = ("registration_number", "owner_name", "brand", "vehicle_model")