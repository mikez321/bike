"""Module used to interact with API and install wheels on a bike."""
import re
from apiconnector import ApiConnector


class WheelInstaller():
    """Wheel installation functions."""

    conn = ApiConnector()

    def install(self, wheel, bike):
        """Install a wheel on the bike or handle error."""
        bike_info = bike.__dict__.copy()
        bike_info['brake_type'] = bike.brakes
        location = 'f_wheel' if wheel.wheel_type == 'front' else 'r_wheel'
        bike_info[location] = wheel.db_ref

        response = self.conn.update_request(f"bikes/{bike.db_ref}/", bike_info)
        
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
