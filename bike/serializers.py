"""Bike serializer."""
from bike.models import Bike
from rest_framework import serializers


class BikeSerializer(serializers.ModelSerializer):
    """Serializer for bike object."""

    def validate(self, data):
        """Extra validations regarding wheels."""
        # Wheel axles must be compatible with bike axles
        if data.get('f_wheel'):
            f_wheel = data['f_wheel']
            if data['f_axle'] != f_wheel.axle:
                raise serializers.ValidationError(
                    "Axle types must match!"
                )
        if data.get('r_wheel'):
            r_wheel = data['r_wheel']
            if data['r_axle'] != r_wheel.axle:
                raise serializers.ValidationError(
                    "Axle types must match!"
                )
        if data.get('f_wheel'):
            f_wheel = data['f_wheel']
            if (f_wheel.is_disc is False and data['brake_type'] != 2
                    or f_wheel.is_disc and data['brake_type'] != 1):
                raise serializers.ValidationError(
                    "Brake types must match!"
                )
        if data.get('r_wheel'):
            r_wheel = data['r_wheel']
            if (r_wheel.is_disc is False and data['brake_type'] == 2
                    or r_wheel.is_disc and data['brake_type'] == 1):
                raise serializers.ValidationError(
                    "Brake types must match!"
                )
        return data

    class Meta:
        model = Bike
        exclude = ['created_at', 'modified_at']
