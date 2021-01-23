"""Test CLI interfaced bike model."""

import unittest
from wheel import FrontWheel, RearWheel


class FrontWheelTest(unittest.TestCase):
    """Test CLI FrontWheel model."""

    def test_it_exists(self):
        """A newly created wheel is an instance of FrontWheel and has attributes."""
        f_wheel_attributes = {
            'id': 1,
            'manufacturer': 'Specialized',
            'model': 'Stout',
            'is_disc': True,
            'tubeless': True,
            'axle': 2,
            'spoke_count': 32,
            'material': 2,
        }
        f_wheel = FrontWheel(f_wheel_attributes)
        self.assertEqual(type(f_wheel), FrontWheel)
        self.assertEqual(f_wheel.db_ref, 1)
        self.assertEqual(f_wheel.manufacturer, 'Specialized')
        self.assertEqual(f_wheel.model, 'Stout')
        self.assertEqual(f_wheel.is_disc, True)
        self.assertEqual(f_wheel.tubeless, True)
        self.assertEqual(f_wheel.axle, 2)
        self.assertEqual(f_wheel.spoke_count, 32)
        self.assertEqual(f_wheel.material, 2)

    def test_front_wheel_properties(self):
        """Testing of model methods and properties."""
        f_wheel_attributes = {
            'id': 1,
            'manufacturer': 'Specialized',
            'model': 'Stout',
            'is_disc': True,
            'tubeless': True,
            'axle': 2,
            'spoke_count': 32,
            'material': 2,
        }
        f_wheel = FrontWheel(f_wheel_attributes)
        self.assertEqual(f_wheel.axle_type, 'ta')
        self.assertEqual(f_wheel.material_type, 'alloy')
        self.assertEqual(f_wheel.wheel_type, 'front')


class RearWheelTest(unittest.TestCase):
    """Test CLI RearWheel model."""

    def test_it_exists(self):
        """A wheel is an instance of RearWheel and has attributes."""
        r_wheel_attributes = {
            'id': 1,
            'manufacturer': 'Specialized',
            'model': 'Stout',
            'is_disc': True,
            'tubeless': True,
            'axle': 2,
            'spoke_count': 32,
            'material': 2,
            'driver': 1,
            'single_speed_only': False,
            'fixed': False
        }
        r_wheel = RearWheel(r_wheel_attributes)
        self.assertEqual(type(r_wheel), RearWheel)
        self.assertEqual(r_wheel.db_ref, 1)
        self.assertEqual(r_wheel.manufacturer, 'Specialized')
        self.assertEqual(r_wheel.model, 'Stout')
        self.assertEqual(r_wheel.is_disc, True)
        self.assertEqual(r_wheel.tubeless, True)
        self.assertEqual(r_wheel.axle, 2)
        self.assertEqual(r_wheel.spoke_count, 32)
        self.assertEqual(r_wheel.material, 2)
        self.assertEqual(r_wheel.driver, 1)
        self.assertEqual(r_wheel.single_speed, False)
        self.assertEqual(r_wheel.fixed, False)

    def test_rear_wheel_properties(self):
        """Testing of model methods and properties."""
        r_wheel_attributes = {
            'id': 1,
            'manufacturer': 'Specialized',
            'model': 'Stout',
            'is_disc': True,
            'tubeless': True,
            'axle': 2,
            'spoke_count': 32,
            'material': 2,
            'driver': 1,
            'single_speed_only': False,
            'fixed': False
        }
        r_wheel = RearWheel(r_wheel_attributes)
        self.assertEqual(r_wheel.axle_type, 'ta')
        self.assertEqual(r_wheel.material_type, 'alloy')
        self.assertEqual(r_wheel.driver_type, 'shimano/sram 11s')
        self.assertEqual(r_wheel.wheel_type, 'rear')


if __name__ == '__main__':
    unittest.main()
