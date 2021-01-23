"""Module used to get bike info from the bike API."""
from apiconnector import ApiConnector
from bike import Bike


class BikeFetcher():
    """Bike retrieval and creation functions."""

    conn = ApiConnector()

    def get_bikes(self):
        """Create bike objects with data from bike API."""
        response = self.conn.get_request('bikes/')
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
        response = self.conn.get_request(f"bikes/{bike_db_ref}")
        bike_info = response.json()
        bike = Bike(bike_info)
        return bike
