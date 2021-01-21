"""Testing for rear wheel serializer."""

from django.test import TestCase
from wheel.models import RearWheel
from wheel.serializers import RearWheelSerializer


class RearWheelSerializerTest(TestCase):
    """Testing for Front Wheel serializer."""

    def setUp(self):
        """Create a wheel to test."""
        self.r_wheel_attributes = {
            "manufacturer": 'DT Swiss',
            "model": '240s',
            "material": 2,
            "driver": 1,
        }
        self.f_wheel = RearWheel.objects.create(**self.r_wheel_attributes)

    def test_serializer_fields(self):
        """Serializer has expected fields."""
        serializer = RearWheelSerializer(
            instance=self.f_wheel,
            data=self.r_wheel_attributes
        )
        self.assertTrue(serializer.is_valid())
        data = serializer.data
        expected_keys = [
            'id',
            'manufacturer',
            'model',
            'spoke_count',
            'is_disc',
            'tubeless',
            'axle',
            'material',
            'driver',
            'single_speed_only',
            'fixed'
        ]
        omitted_keys = [
            'created_at',
            'modified_at',
        ]
        self.assertEqual(set(data.keys()), set(expected_keys))
        for key in omitted_keys:
            self.assertFalse(key in data.keys())
