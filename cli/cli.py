"""CLI tool for interacting with the API."""

from bikefetcher import BikeFetcher
from wheelfetcher import WheelFetcher
from wheelinstaller import WheelInstaller
from termcolor import colored
import time


def bike_details(bike):
    """Return details of a given bike."""
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
    print(f"\nBike: {bike.make} {bike.model}")
    print("_" * 40)
    print(f"-Type: {bike.bike_type.capitalize()}")
    print(f"-Brakes: {bike.brake_type.capitalize()}")
    print(f"-Front Axle: {bike.front_axle_type.capitalize()}")
    print(f"-Rear_Axle: {bike.rear_axle_type.capitalize()}")
    print(f"-Front Wheel: {f_wheel}")
    print(f"-Rear Wheel: {r_wheel}")

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

    if bike.f_wheel is not None and bike.r_wheel is not None:
        print('*' * 40)
        bike_details(bike)
        print('*' * 40)
        print("One bike... two wheels... all set!")
        break
    else:
        bike_details(bike)
        print("\nAvailable Wheels:")
        print("_" * 40)
        for option, wheel in wheel_dict.items():
            print(f"{option}:\t{wheel.manufacturer} {wheel.model} ({wheel.wheel_type}/{wheel.axle_type})")
        print("\n Chose a wheel to install on the bike, or press 'q' at any time to exit.")
        choice = input()
        if choice.casefold() == 'q':
            print("Bye!")
            break
        elif choice.isnumeric() is False or int(choice) not in wheel_dict.keys():
            time.sleep(3)
            print("\n" * 2)
            print("*" * 40)
            print("Plese select a valid wheel option or press 'q' to exit.")
            print("*" * 40)
        else:
            wheel_choice = int(choice)
            wheel = wheel_dict[wheel_choice]
            print()
            print(f"Installing {wheel.manufacturer} {wheel.model} on {bike.make} {bike.model}...")
            time.sleep(3)
            wheelinstaller = WheelInstaller()
            print(wheelinstaller.install(wheel, bike))
