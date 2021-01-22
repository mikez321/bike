from bike import Bike
from wheel import FrontWheel, RearWheel
import requests
import json
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
print(f"Bike: {bike.make} {bike.model}")
print(f"-Type: {bike.bike_type.capitalize()}")
print(f"-Brakes: {bike.brake_type.capitalize()}")
print(f"-Front Axle: {bike.front_axle_type.capitalize()}")
print(f"-Rear_Axle: {bike.rear_axle_type.capitalize()}")
print()
print("Available Wheels:")
for option, wheel in wheel_dict.items():
    print(f"{option}:\t{wheel.manufacturer} {wheel.model}")
wheel_choice = input("Choose a rear wheel to install: ")
wheel = wheel_dict[int(wheel_choice)]
print()
print(f"Installing {wheel.manufacturer} {wheel.model} on {bike.make} {bike.model}")
