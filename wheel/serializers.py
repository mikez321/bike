"""Wheel serializer."""
from wheel.models import FrontWheel, RearWheel
from rest_framework import serializers


class GenericWheelSerializer(serializers.Serializer):
    """Generic wheel serializer for all wheels list view."""

    type = serializers.SerializerMethodField()
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=30,
    )
    model = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=30,
    )

    def get_type(self, obj):
        """Return class name of an object for identification."""
        return obj.__class__.__name__


class FrontWheelSerializer(serializers.ModelSerializer):
    """Serializer for FrontWheel object."""

    class Meta:
        model = FrontWheel
        exclude = ['created_at', 'modified_at']


class RearWheelSerializer(serializers.ModelSerializer):
    """Serializer for RearWheel object."""

    def validate(self, data):
        """Declare extra validations."""
        if (data.get('fixed') or data.get('single_speed_only')
                and data['driver'] != 6):
            raise serializers.ValidationError(
                "Invalid combination of rear hub drivers."
            )
        if data.get('fixed') and data.get('single_speed_only'):
            raise serializers.ValidationError(
                "Fixed hubs are not the same as single speed hubs."
            )
        return data

    class Meta:
        model = RearWheel
        exclude = ['created_at', 'modified_at']
