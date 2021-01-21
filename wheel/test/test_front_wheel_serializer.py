"""Testing for front wheel serializer."""

from django.test import TestCase
from wheel.models import FrontWheel
from wheel.serializers import FrontWheelSerializer


class FrontWheelSerializerTest(TestCase):
    """Testing for Front Wheel serializer."""

    def setUp(self):
        """Create a wheel to test."""
        self.f_wheel_attributes = {
            "manufacturer": 'DT Swiss',
            "model": '240s',
            "material": 2,
        }
        self.f_wheel = FrontWheel.objects.create(**self.f_wheel_attributes)

    def test_serializer_fields(self):
        """Serializer has expected fields."""
        serializer = FrontWheelSerializer(
            instance=self.f_wheel,
            data=self.f_wheel_attributes
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
        ]
        omitted_keys = [
            'created_at',
            'modified_at',
        ]
        self.assertEqual(set(data.keys()), set(expected_keys))
        for key in omitted_keys:
            self.assertFalse(key in data.keys())
