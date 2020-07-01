from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
from .models import Carsforsale

class CarsforsaleAdmin(admin.ModelAdmin):
    list_display = ("title", "make", "model", "manufactured", "transmission","car_description", "fuel_type", "color")
    list_filter= ("make", "model", "manufactured", "transmission", "fuel_type", "color")
    search_fields =("make", "model", "manufactured", "transmission", "car_description", "fuel_type", "color")

admin.site.site_header = "Gumtree admin"
admin.site.register(Carsforsale, CarsforsaleAdmin)
