"""Module used to get wheel information from bike API."""
import requests
from wheel import FrontWheel, RearWheel


class WheelFetcher():
    """Wheel retrieval functions."""

    def get_front_wheels(self):
        """Return all front wheels from the API as front wheel objects."""
        response = requests.get('http://localhost:8000/wheels/front')
        wheel_info = response.json()
        front_wheels = []
        for wheel_attributes in wheel_info:
            wheel = FrontWheel(wheel_attributes)
            front_wheels.append(wheel)
        return front_wheels

    def get_rear_wheels(self):
        """Return all rear wheels from the api as rear wheel objects."""
        response = requests.get('http://localhost:8000/wheels/rear')
        wheel_info = response.json()
        rear_wheels = []
        for wheel_attributes in wheel_info:
            wheel = RearWheel(wheel_attributes)
            rear_wheels.append(wheel)
        return rear_wheels

    def get_wheels(self):
        """Compile rear wheels and front wheels into a single list."""
        fronts = self.get_front_wheels()
        rears = self.get_rear_wheels()
        all = fronts + rears
        option = 1
        wheel_dict = {}
        for wheel in all:
            wheel_dict[option] = wheel
            option += 1
        return wheel_dict
