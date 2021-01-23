"""Module used to get bike info from the bike API."""
import requests
from bike import Bike


class BikeFetcher():
    """Bike retrieval and creation functions."""

    def get_bikes(self):
        """Create bike objects with data from bike API."""
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
        """Create a single bike with data from the bike API."""
        response = requests.get(f"http://localhost:8000/bikes/{bike_db_ref}")
        bike_info = response.json()
        bike = Bike(bike_info)
        return bike
