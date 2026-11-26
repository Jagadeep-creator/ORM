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