"""CLI tool for interacting with the API."""

from bike import Bike
from wheel import FrontWheel, RearWheel
import requests
import time
import re
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

    def get_bike(self, bike_db_ref):
        response = requests.get(f"http://localhost:8000/bikes/{bike_db_ref}")
        bike_info = response.json()
        bike = Bike(bike_info)
        return bike


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
        bike_info = bike.__dict__.copy()
        bike_info['brake_type'] = bike.brakes
        location = 'f_wheel' if wheel.wheel_type == 'front' else 'r_wheel'
        bike_info[location] = wheel.db_ref
        response = requests.patch(
            f"http://localhost:8000/bikes/{bike.db_ref}/",
            bike_info,
        )
        if response.status_code == 200:
            return f"{wheel.model.capitalize()} was installed!"
        if response.status_code == 400:
            if 'field_errors' in response.content.decode():
                error = response.content.decode().split('[')[1]
                result = re.findall('[A-z \s !]+', error)
                return result[0]
            else:
                return "Looks like that wheel might not be compatible or one might already be on the bike."
        else:
            return "Something went wrong. Try again..."


bikefetcher = BikeFetcher()
wheelfetcher = WheelFetcher()
bike_dict = bikefetcher.get_bikes()
wheel_dict = wheelfetcher.get_wheels()
print("\n" * 2)
print("*" * 50)
print("Hey! Let's put some wheels on a bike!")
print("*" * 50)
while True:
    print("Available Bikes:")
    for option, bike in bike_dict.items():
        print(f"{option}:\t{bike.make} {bike.model}")
    choice = input("\nChoose a bike: ")
    if choice.isnumeric() is False or int(choice) not in bike_dict.keys():
        print("*" * 40)
        print("Plese select a valid bike option to get started.")
        print("*" * 40)
    else:
        bike_choice = int(choice)
        chosen_bike_db_ref = bike_dict[bike_choice].db_ref
        break

while True:
    bike = bikefetcher.get_bike(chosen_bike_db_ref)
    if bike.f_wheel:
        f_wheel = list(
            filter(
                lambda w: w.db_ref == bike.f_wheel, wheel_dict.values()
            )
        )[0]
    else:
        f_wheel = ' -- '
    if bike.r_wheel:
        r_wheel = list(
            filter(
                lambda w: w.db_ref == bike.r_wheel, wheel_dict.values()
            )
        )[0]
    else:
        r_wheel = ' -- '

    if bike.f_wheel is not None and bike.r_wheel is not None:
        print('*' * 40)
        print(f"\nBike: {bike.make} {bike.model}")
        print("_" * 40)
        print(f"-Type: {bike.bike_type.capitalize()}")
        print(f"-Brakes: {bike.brake_type.capitalize()}")
        print(f"-Front Axle: {bike.front_axle_type.capitalize()}")
        print(f"-Rear_Axle: {bike.rear_axle_type.capitalize()}")
        print(f"-Front Wheel: {f_wheel}")
        print(f"-Rear Wheel: {r_wheel}")
        print('*' * 40)
        print("One bike... two wheels... all set!")
        break
    else:
        print(f"\nBike: {bike.make} {bike.model}")
        print("_" * 40)
        print(f"-Type: {bike.bike_type.capitalize()}")
        print(f"-Brakes: {bike.brake_type.capitalize()}")
        print(f"-Front Axle: {bike.front_axle_type.capitalize()}")
        print(f"-Rear_Axle: {bike.rear_axle_type.capitalize()}")
        print(f"-Front Wheel: {f_wheel}")
        print(f"-Rear Wheel: {r_wheel}")
        print()
        print("Available Wheels:")
        print("_" * 40)
        for option, wheel in wheel_dict.items():
            print(f"{option}:\t{wheel.manufacturer} {wheel.model} ({wheel.wheel_type}/{wheel.axle_type})")
        print("\n Chose a wheel to install on the bike, or press 'q' at any time to exit.")
        choice = input()
        if choice.casefold() == 'q':
            print("Bye!")
            break
        elif choice.isnumeric() is False or int(choice) not in wheel_dict.keys():
            time.sleep(1)
            print("\n" * 2)
            print("*" * 40)
            print("Plese select a valid wheel option or press 'q' to exit.")
            print("*" * 40)
        else:
            wheel_choice = int(choice)
            wheel = wheel_dict[wheel_choice]
            print()
            print(f"Installing {wheel.manufacturer} {wheel.model} on {bike.make} {bike.model}")
            time.sleep(1)
            wheelinstaller = WheelInstaller()
            print(wheelinstaller.install(wheel, bike))
