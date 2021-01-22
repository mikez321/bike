"""Test CLI interfaced bike model."""

import unittest
from bike import Bike


class BikeTest(unittest.TestCase):
    """Test CLI Bike model."""

    def test_it_exists(self):
        """A newly created bike is an instance of Bike and has attributes."""
        bike_attributes = {
            'id': 1,
            'make': 'Specialized',
            'model': 'Chisel',
            'type': 2,
            'description': "It's a hardtail 29er.",
            'brake_type': 1,
            'f_axle': 2,
            'r_axle': 2,
            'f_wheel': None,
            'r_wheel': None
        }
        bike = Bike(bike_attributes)
        self.assertEqual(type(bike), Bike)
        self.assertEqual(bike.db_ref, 1)
        self.assertEqual(bike.make, 'Specialized')
        self.assertEqual(bike.model, 'Chisel')
        self.assertEqual(bike.type, 2)
        self.assertEqual(bike.description, "It's a hardtail 29er.")
        self.assertEqual(bike.f_axle, 2)
        self.assertEqual(bike.r_axle, 2)
        self.assertEqual(bike.brakes, 1)
        self.assertEqual(bike.f_wheel, None)
        self.assertEqual(bike.r_wheel, None)

    def test_bike_properties(self):
        """Testing of model methods and properties."""
        bike_attributes = {
            'id': 1,
            'make': 'Specialized',
            'model': 'Chisel',
            'type': 2,
            'description': "It's a hardtail 29er.",
            'f_axle': 2,
            'r_axle': 2,
            'brake_type': 1,
            'f_wheel': None,
            'r_wheel': None
        }
        bike = Bike(bike_attributes)
        self.assertEqual(bike.bike_type, "mountain")
        self.assertEqual(bike.brake_type, "disc")
        self.assertEqual(bike.front_axle_type, "thru")
        self.assertEqual(bike.rear_axle_type, "thru")


if __name__ == '__main__':
    unittest.main()
