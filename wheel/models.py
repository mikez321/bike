"""Wheel and wheel related models."""
from django.db import models


class GenericWheel(models.Model):
    """A generic wheel model that specialty wheels can inherit from."""
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
