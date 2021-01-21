"""Admin site setup for wheels."""
from django.contrib import admin
from wheel.models import FrontWheel, RearWheel


admin.site.register(FrontWheel)
admin.site.register(RearWheel)
