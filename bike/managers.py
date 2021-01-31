"""Custom managers for bike objects."""

from django.db import models


class RoadBikeManager(models.Manager):
    """Custom manager for road bikes."""

    def get_queryset(self):
        """Return only road bikes."""
        return super().get_queryset().filter(type=1)


class MountainBikeManager(models.Manager):
    """Custom manager for road bikes."""

    def get_queryset(self):
        """Return only mountain bikes."""
        return super().get_queryset().filter(type=2)
