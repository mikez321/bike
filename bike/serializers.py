"""Bike serializer."""
from bike.models import Bike
from rest_framework import serializers


class BikeSerializer(serializers.ModelSerializer):
    """Serializer for bike object."""

    class Meta:
        model = Bike
        exclude = ['created_at', 'modified_at']
