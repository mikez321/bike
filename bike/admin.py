"""Admin site setup for bike app."""
from django.contrib import admin
from bike.models import Bike


admin.site.register(Bike)
