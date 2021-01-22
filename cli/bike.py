"""Bike class representation for CLI."""
from IPython import embed

class Bike(object):
    """Bike object to be created from json response."""

    def __init__(self, attributes):
        """Initialize bike object from a dictionatry of attributes."""
        self.make = attributes['make']
        self.model = attributes['model']
        self.type = attributes['type']
        self.description = attributes['description']
        self.brakes = attributes['brake_type']
        self.f_axle = attributes['f_axle']
        self.r_axle = attributes['r_axle']
        self.f_wheel = None
        self.r_wheel = None

    @property
    def bike_type(self):
        """Return string representation of bike type."""
        BIKE_TYPES = {
            1: 'road',
            2: 'mountain',
            3: 'hybrid',
            4: 'comfort/cruiser',
            5: 'e-bike',
            6: 'other',
        }
        return BIKE_TYPES[self.type]

    @property
    def brake_type(self):
        """Return string representation of bike brake type."""
        BRAKE_TYPES = {
            1: 'disc',
            2: 'rim',
        }
        return BRAKE_TYPES[self.brakes]

    @property
    def front_axle_type(self):
        AXLE_TYPES = {
            1: 'qr',
            2: 'thru',
            3: 'other',
        }
        return AXLE_TYPES[self.f_axle]

    @property
    def rear_axle_type(self):
        AXLE_TYPES = {
            1: 'qr',
            2: 'thru',
            3: 'other',
        }
        return AXLE_TYPES[self.r_axle]
