from bike import Bike
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

class WheelFetcher()
    def get_wheels(self):
        


bikefetcher = BikeFetcher()
bike_dict = bikefetcher.get_bikes()
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
