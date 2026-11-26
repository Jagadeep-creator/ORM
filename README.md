# Ex02 Django ORM Web Application
## Date: 26-11-26

## AIM
To develop a Django Application to store and retrieve data from a Vehicle Service Database platform using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
admin.py 
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
    
    models.py
    from django.db import models


class VehicleService(models.Model):
    # (value stored in DB, label shown to people)
    VEHICLE_TYPES = [
        ("2W", "Two Wheeler"),
        ("4W", "Four Wheeler"),
        ("CV", "Commercial Vehicle"),
    ]
    SERVICE_TYPES = [
        ("GEN", "General Service"),
        ("OIL", "Oil Change"),
        ("BRK", "Brake Repair"),
        ("TYR", "Tyre Replacement"),
        ("ENG", "Engine Repair"),
    ]
    STATUS_CHOICES = [
        ("PEN", "Pending"),
        ("INP", "In Progress"),
        ("COM", "Completed"),
    ]

    registration_number = models.CharField(max_length=15)
    owner_name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=2, choices=VEHICLE_TYPES, default="4W")
    brand = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=50)
    service_type = models.CharField(max_length=3, choices=SERVICE_TYPES, default="GEN")
    service_date = models.DateField()
    odometer_reading = models.PositiveIntegerField(help_text="Distance covered, in km")
    service_cost = models.DecimalField(max_digits=8, decimal_places=2, help_text="Amount in INR")
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default="PEN")
    remarks = models.TextField(blank=True)

    class Meta:
        ordering = ["-service_date"]
        verbose_name = "Vehicle Service"
        verbose_name_plural = "Vehicle Services"

    def __str__(self):
        return f"{self.registration_number} - {self.get_service_type_display()}"    
```


## OUTPUT

![alt text](<Screenshot 2026-11-26 101339.png>)


## RESULT
Thus the program for creating vehicle service Database using ORM hss been executed successfully.
