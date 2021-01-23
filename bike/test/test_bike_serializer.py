"""Testing for BikeSerializer."""

from django.test import TestCase
from bike.serializers import BikeSerializer
from bike.models import Bike
from wheel.models import FrontWheel, RearWheel
from django.db import transaction


class BikeSerializerTest(TestCase):
    """Testing for bike serializer."""

    def setUp(self):
        """Declare up some attributes and use them to create a bike."""
        self.bike_attributes = {
            'make': 'Fairdale',
            'model': 'Goodship',
            'type': 1,
            'description': 'A steel and carbon road bike.',
            'brake_type': 2,
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
            'brake_type',
            'brake_type',
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
        f_wheel = FrontWheel(**self.f_wheel_attributes)
        r_wheel = RearWheel(**self.r_wheel_attributes)
        bike_attributes = self.bike_attributes

        bike = Bike(**bike_attributes)
        try:
            with transaction.atomic():
                bike.f_wheel = r_wheel
            self.fail("Rear wheels can't go on the front.")
        except ValueError:
            pass
        try:
            with transaction.atomic():
                bike.r_wheel = f_wheel
            self.fail("Front wheels can't go on the rear.")
        except ValueError:
            pass

    def test_custom_validations(self):
        """Axle types must match."""
        f_wheel_attributes = self.f_wheel_attributes
        bike_attributes = self.bike_attributes

        f_wheel_attributes['axle'] = 2
        wheel_fail1 = FrontWheel.objects.create(**f_wheel_attributes)
        bike_attributes['f_wheel'] = wheel_fail1

        # Wheel now has axle type2 (thru-axle) and bike has axle type 1 (QR)

        serializer = BikeSerializer(
            instance=self.bike,
            data=bike_attributes
        )
        self.assertFalse(serializer.is_valid())
        self.assertTrue(
            'Axle types must match!' in serializer.errors['non_field_errors']
        )

    def test_more_custom_validations(self):
        """Brake types must match between wheels and bikes."""
        bike_attributes = self.bike_attributes
        f_wheel = FrontWheel.objects.create(**self.f_wheel_attributes)
        bike_attributes['brake_type'] = 1
        bike_attributes['f_wheel'] = f_wheel

        fail_bike = Bike(**bike_attributes)
        self.assertEqual(f_wheel.is_disc, False)
        self.assertEqual(fail_bike.get_brake_type_display(), "Disc")
        serializer = BikeSerializer(
            instance=fail_bike,
            data=bike_attributes
        )
        self.assertFalse(serializer.is_valid())
        self.assertTrue(
            'Brake types must match!' in serializer.errors['non_field_errors']
        )
