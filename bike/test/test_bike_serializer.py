"""Testing for BikeSerializer."""

from django.test import TestCase
from bike.serializers import BikeSerializer
from bike.models import Bike


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
        self.bike = Bike.objects.create(**self.bike_attributes)

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
        ]
        omitted_keys = [
            'created_at',
            'modified_at',
        ]
        self.assertEqual(set(data.keys()), set(expected_keys))
        for key in omitted_keys:
            self.assertFalse(key in data.keys())
