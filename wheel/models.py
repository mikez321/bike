"""Wheel and wheel related models."""
from django.db import models


class GenericWheel(models.Model):
    """A generic wheel model that specialty wheels can inherit from."""

    WHEEL_AXLE_CHOICES = [
        (1, "QR"),
        (2, "Thru"),
        (3, "Other"),
    ]
    WHEEL_MATERIAL_OPTIONS = [
        (1, "Carbon"),
        (2, "Alloy"),
        (3, "Other"),
    ]

    spoke_count = models.PositiveIntegerField(
        default=32,
        blank=True,
        null=True,
    )
    manufacturer = models.CharField(max_length=30, blank=False, null=False)
    model = models.CharField(max_length=30, blank=False, null=False)
    is_disc = models.BooleanField(default=True, blank=True, null=True)
    tubeless = models.BooleanField(default=True, blank=True, null=True)
    axle = models.IntegerField(
        choices=WHEEL_AXLE_CHOICES,
        default=3,
        blank=False,
        null=False,
    )
    material = models.IntegerField(
        choices=WHEEL_MATERIAL_OPTIONS,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Magic string method."""
        return f"Generic wheel with {self.spoke_count} spokes."


class FrontWheel(GenericWheel):
    """Specific front wheel model inheriting fom generic wheel model."""

    def __str__(self):
        """Magic string method."""
        brake = "Disc" if self.is_disc else "Rim"
        return f"{self.manufacturer} {self.model} {brake} Front Wheel"


class RearWheel(GenericWheel):
    """Specific rear wheel model inheriting fom generic wheel model."""

    FREEHUB_CHOICES = [
        (1, "Shimano/SRAM 11s"),
        (2, "XD"),
        (3, "XDR"),
        (4, "Shimano Micro Spline"),
        (5, "Campagnolo"),
    ]
    driver = models.IntegerField(
        choices=FREEHUB_CHOICES,
        blank=False,
        null=False,
    )
    single_speed_only = models.BooleanField(
        default=False,
        blank=False,
        null=False
    )
    fixed = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        """Magic string method."""
        brake = "Disc" if self.is_disc else "Rim"
        return f"{self.manufacturer} {self.model} {brake} Rear Wheel"
