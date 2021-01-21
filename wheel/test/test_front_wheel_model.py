"""Testing for wheel model."""

from django.test import TestCase
from wheel.models import FrontWheel


class FrontWheelModelTest(TestCase):
    """Testing for Front Wheel model and associated model methods."""

    def setUp(self):
        """Create a wheel to test."""
        self.f_wheel = FrontWheel.objects.create(
            manufacturer='DT Swiss',
            model='240s',
            material=2,
        )

    def test_attributes(self):
        """Test attributes including defaults."""
        wheel = FrontWheel.objects.first()
        self.assertEqual(wheel.manufacturer, 'DT Swiss')
        self.assertEqual(wheel.model, '240s')
        self.assertEqual(wheel.spoke_count, 32)
        self.assertTrue(wheel.is_disc)
        self.assertTrue(wheel.tubeless)
        self.assertEqual(wheel.axle, 3)
        self.assertEqual(wheel.get_axle_display(), 'Other')
        self.assertEqual(wheel.material, 2)
        self.assertEqual(wheel.get_material_display(), 'Alloy')
