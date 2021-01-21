"""Wheel serializer."""
from wheel.models import FrontWheel, RearWheel
from rest_framework import serializers


class FrontWheelSerializer(serializers.ModelSerializer):
    """Serializer for FrontWheel object."""

    class Meta:
        model = FrontWheel
        exclude = ['created_at', 'modified_at']


class RearWheelSerializer(serializers.ModelSerializer):
    """Serializer for RearWheel object."""

    class Meta:
        model = RearWheel
        exclude = ['created_at', 'modified_at']
