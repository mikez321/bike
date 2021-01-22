"""Testing for BikeSerializer."""

from django.test import TestCase
from bike.serializers import BikeSerializer
from bike.models import Bike
from wheel.models import FrontWheel, RearWheel
from IPython import embed


class BikeSerializerTest(TestCase):
    """Testing for bike serializer."""

    def setUp(self):
        """Declare up some attributes and use them to create a bike."""
        self.bike_attributes = {
            'make': 'Fairdale',
            'model': 'Goodship',
            'type': 1,
            'description': 'A steel and carbon road bike.',
            'f_axle': 1,
            'r_axle': 1,
        }
        self.f_wheel_attributes = {
            'manufacturer': 'Zipp',
            'model': '202',
            'material': '1',
            'spoke_count': 18,
            'is_disc': False,
            'tubeless': False,
            'axle': 1,
        }

        self.r_wheel_attributes = {
            'manufacturer': 'Zipp',
            'model': '202',
            'material': '1',
            'spoke_count': 18,
            'is_disc': False,
            'tubeless': False,
            'axle': 1,
            'driver': 1,
        }
        self.bike = Bike.objects.create(**self.bike_attributes)
        self.r_wheel = RearWheel.objects.create(**self.r_wheel_attributes)
        self.f_wheel = FrontWheel.objects.create(**self.f_wheel_attributes)

    def test_serializer_fields(self):
        """Serializer has expected fields."""
        serializer = BikeSerializer(
            instance=self.bike,
            data=self.bike_attributes
        )
        self.assertTrue(serializer.is_valid())
        data = serializer.data
        expected_keys = [
            'id',
            'make',
            'model',
            'type',
            'description',
            'f_axle',
            'r_axle',
            'f_wheel',
            'r_wheel',
        ]
        omitted_keys = [
            'created_at',
            'modified_at',
        ]
        self.assertEqual(set(data.keys()), set(expected_keys))
        for key in omitted_keys:
            self.assertFalse(key in data.keys())

    def test_validations(self):
        """Front wheels only go on the front, rears on the rear."""
        self.bike_attributes['f_wheel'] = self.r_wheel.id
        serializer = BikeSerializer(
            instance=self.bike,
            data=self.bike_attributes
        )
        self.assertFalse(serializer.is_valid())

        self.bike_attributes['f_wheel'] = None
        self.bike_attributes['r_wheel'] = self.f_wheel.id
        serializer = BikeSerializer(
            instance=self.bike,
            data=self.bike_attributes
        )
        self.assertFalse(serializer.is_valid())

        self.bike_attributes['f_wheel'] = self.f_wheel.id
        self.bike_attributes['r_wheel'] = self.r_wheel.id
        serializer = BikeSerializer(
            instance=self.bike,
            data=self.bike_attributes
        )
        self.assertTrue(serializer.is_valid())
