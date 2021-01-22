"""Bike serializer."""
from bike.models import Bike
from rest_framework import serializers
from IPython import embed


class BikeSerializer(serializers.ModelSerializer):
    """Serializer for bike object."""

    def validate(self, data):
        """Extra validations regarding wheels."""
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
        return data


    class Meta:
        model = Bike
        exclude = ['created_at', 'modified_at']
