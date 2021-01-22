"""Wheel object."""
from IPython import embed

class Wheel(object):
    """A regular 'ol wheel."""

    def __init__(self, f_wheel_attributes):
        """Front wheel object created from json response."""
        self.manufacturer = f_wheel_attributes['manufacturer']
        self.model = f_wheel_attributes['model']
        self.is_disc = f_wheel_attributes['is_disc']
        self.tubeless = f_wheel_attributes['tubeless']
        self.axle = f_wheel_attributes['axle']
        self.spoke_count = f_wheel_attributes['spoke_count']
        self.material = f_wheel_attributes['material']

    @property
    def axle_type(self):
        """Return a string representation of axle type."""
        AXLE_TYPES = {
            1: "qr",
            2: "thru",
            3: "other",
        }
        return AXLE_TYPES[self.axle]

    @property
    def material_type(self):
        """Return a string representation of material type."""
        MATERIAL_TYPES = {
            1: "carbon",
            2: "alloy",
            3: "other",
        }
        return MATERIAL_TYPES[self.material]


class FrontWheel(Wheel):
    """A front wheel is basically a generic wheel."""


class RearWheel(Wheel):
    """A rear wheel object."""

    def __init__(self, r_wheel_attributes):
        """All the same stuff as a regular wheel and a few extras."""
        super().__init__(r_wheel_attributes)
        self.driver = r_wheel_attributes['driver']
        self.single_speed = r_wheel_attributes['single_speed']
        self.fixed = r_wheel_attributes['fixed']

    @property
    def driver_type(self):
        """Return a string representation of driver type."""
        DRIVER_TYPES = {
            1: "shimano/sram 11s",
            2: "xd",
            3: "xdr",
            4: "shimano micro spline",
            5: "campagnolo",
            6: "other",
        }
        return DRIVER_TYPES[self.driver]
