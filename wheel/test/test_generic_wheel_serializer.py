"""Testing for generic wheel serializer."""

from django.test import TestCase
from wheel.serializers import GenericWheelSerializer
from wheel.models import FrontWheel, RearWheel


class GenericWheelSerializerTest(TestCase):
    """Testing for Generic Wheel serializer."""

    def setUp(self):
        """Create some wheels (f and r) to test."""
        self.wheel_attributes1 = {
            'manufacturer': 'DT Swiss',
            'model': '240s',
            'axle': 2,
            'material': 2,
            'driver': 1,
        }
        self.wheel_attributes2 = {
            'manufacturer': 'ENVE',
            'model': 'M630',
            'axle': 2,
            'material': 1,
            'driver': 2,
        }
        self.wheel_attributes3 = {
            'manufacturer': 'Zipp',
            'model': '303',
            'axle': 2,
            'material': 1,
        }
        self.wheel1 = RearWheel.objects.create(**self.wheel_attributes1)
        self.wheel2 = RearWheel.objects.create(**self.wheel_attributes2)
        self.wheel3 = FrontWheel.objects.create(**self.wheel_attributes3)

    def test_serializer_fields(self):
        """Serializer has expected fields."""
        serializer1 = GenericWheelSerializer(instance=self.wheel1,
                                             data=self.wheel_attributes1)
        serializer2 = GenericWheelSerializer(instance=self.wheel2,
                                             data=self.wheel_attributes2)
        serializer3 = GenericWheelSerializer(instance=self.wheel3,
                                             data=self.wheel_attributes3)
        serializers = [serializer1, serializer2, serializer3]

        for serializer in serializers:
            self.assertTrue(serializer.is_valid())
            data = serializer.data
            expected_keys = [
                'id',
                'type',
                'manufacturer',
                'model'
            ]
            self.assertEqual(set(data.keys()), set(expected_keys))
