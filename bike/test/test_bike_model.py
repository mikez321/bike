"""Testing for bike model."""

from django.test import TestCase
from .. models import Bike


class BikeModelTest(TestCase):
    """Testing for bike model and model methods."""

    def setUp(self):
        """Create a bike to test."""
        self.bike = Bike.objects.create(
            make='Specialized',
            model='Chisel',
            type=2,
            description="It's a hardtail 29er.",
            f_axle=2,
            r_axle=2,
        )
        self.bike = Bike.objects.create(
            make='Fairdale',
            model='Goodship',
            type=1,
            description='A steel and carbon road bike.',
            brake_type=2,
            f_axle=1,
            r_axle=1,
        )

    def test_attributes(self):
        """Bikes have attributes."""
        bike = Bike.objects.first()
        self.assertEqual(bike.make, 'Specialized')
        self.assertEqual(bike.model, 'Chisel')
        self.assertEqual(bike.type, 2)
        self.assertEqual(bike.get_type_display(), 'Mountain')
        self.assertEqual(bike.description, "It's a hardtail 29er.")
        self.assertEqual(bike.f_axle, 2)
        self.assertEqual(bike.r_axle, 2)
        self.assertEqual(bike.brake_type, 1)
        self.assertEqual(bike.get_brake_type_display(), "Disc")
        self.assertEqual(bike.get_f_axle_display(), 'Thru')
        self.assertEqual(bike.get_r_axle_display(), 'Thru')
