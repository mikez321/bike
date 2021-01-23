"""CLI tool for interacting with the API."""

from bike import Bike
from wheel import FrontWheel, RearWheel
import requests
from IPython import embed


class BikeFetcher():
    def get_bikes(self):
        response = requests.get('http://localhost:8000/bikes/')
        bike_info = response.json()
        option = 1
        bike_dict = {}
        for bike_attributes in bike_info:
            bike = Bike(bike_attributes)
            bike_dict[option] = bike
            option += 1
        return bike_dict


class WheelFetcher():
    def get_front_wheels(self):
        response = requests.get('http://localhost:8000/wheels/front')
        wheel_info = response.json()
        front_wheels = []
        for wheel_attributes in wheel_info:
            wheel = FrontWheel(wheel_attributes)
            front_wheels.append(wheel)
        return front_wheels

    def get_rear_wheels(self):
        response = requests.get('http://localhost:8000/wheels/rear')
        wheel_info = response.json()
        rear_wheels = []
        for wheel_attributes in wheel_info:
            wheel = RearWheel(wheel_attributes)
            rear_wheels.append(wheel)
        return rear_wheels

    def get_wheels(self):
        fronts = self.get_front_wheels()
        rears = self.get_rear_wheels()
        all = fronts + rears
        option = 1
        wheel_dict = {}
        for wheel in all:
            wheel_dict[option] = wheel
            option += 1
        return wheel_dict


class WheelInstaller():
    """Install a wheel on a bike through the API."""

    def install(self, wheel, bike):
        """Install a wheel on the bike or handle error."""
        bike_info = bike.__dict__
        bike_info['brake_type'] = bike.brakes
        location = 'f_wheel' if wheel.wheel_type == 'front' else 'r_wheel'
        bike_info[location] = wheel.db_ref
        response = requests.patch(
            f"http://localhost:8000/bikes/{bike.db_ref}/",
            bike_info,
        )
        if response.status_code == 200:
            return "Install went smooth!"
        else:
            return "Something went wrong..."


bikefetcher = BikeFetcher()
wheelfetcher = WheelFetcher()
bike_dict = bikefetcher.get_bikes()
wheel_dict = wheelfetcher.get_wheels()
print("\n" * 5)
print("*" * 60)
print("Hey! Let's put some wheels on a bike!")
print("*" * 60)
print()
print("Available Bikes:")
for option, bike in bike_dict.items():
    print(f"{option}:\t{bike.make} {bike.model}")
print()
bike_choice = input("Choose a bike: ")
bike = bike_dict[int(bike_choice)]
while True:
    if bike.f_wheel is not None and bike.r_wheel is not None:
        print("One bike... two wheels... all set!")
        break
    else:
        print(f"Bike: {bike.make} {bike.model}")
        print(f"-Type: {bike.bike_type.capitalize()}")
        print(f"-Brakes: {bike.brake_type.capitalize()}")
        print(f"-Front Axle: {bike.front_axle_type.capitalize()}")
        print(f"-Rear_Axle: {bike.rear_axle_type.capitalize()}")
        current_f_wheel = 'installed' if bike.f_wheel else ' -- '
        print(f"-Front Wheel: {current_f_wheel.capitalize()}")
        current_r_wheel = 'installed' if bike.r_wheel else ' -- '
        print(f"-Rear Wheel: {current_r_wheel.capitalize()}")
        print()
        print("Available Wheels:")
        for option, wheel in wheel_dict.items():
            print(f"{option}:\t{wheel.manufacturer} {wheel.model} ({wheel.wheel_type}/{wheel.axle_type})")
        wheel_choice = input("Choose a wheel to install: ")
        wheel = wheel_dict[int(wheel_choice)]
        print()
        print(f"Installing {wheel.manufacturer} {wheel.model} on {bike.make} {bike.model}")
        wheelinstaller = WheelInstaller()
        print(wheelinstaller.install(wheel, bike))
