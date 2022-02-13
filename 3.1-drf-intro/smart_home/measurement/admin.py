from csv import list_dialects
from django.contrib import admin

from measurement.models import Measurement, Sensor

# Register your models here.
@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ("id","temperature", "created_at")
