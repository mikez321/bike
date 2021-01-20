"""Bike app models found here."""
from django.db import models


class Bike(models.Model):
    """A basic bike model."""

    BIKE_TYPE_CHOICES = [
        (1, 'Road'),
        (2, 'Mountain'),
        (3, 'Hybrid'),
        (4, 'Comfort/Cruiser'),
        (5, 'E-Bike'),
        (6, 'Other'),
    ]
    AXLE_TYPE_CHOICES = [
        (1, 'QR'),
        (2, 'Thru'),
    ]
    make = models.CharField(max_length=30, blank=False, null=False)
    model = models.CharField(max_length=30, blank=False, null=False)
    type = models.IntegerField(
        choices=BIKE_TYPE_CHOICES,
        blank=False,
        null=False
    )
    description = models.TextField(max_length=200, blank=True, null=True)
    f_axle = models.IntegerField(
        choices = AXLE_TYPE_CHOICES,
        blank=False,
        null=False,
    )
    r_axle = models.IntegerField(
        choices = AXLE_TYPE_CHOICES,
        blank=False,
        null=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Magic string method."""
        return f"{self.make} {self.model}"