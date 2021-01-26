"""A single module to interact with the API."""

import requests


class ApiConnector():
    """Reusable module allowing connection to the bike API."""

    destination = 'http://bike-api-env.us-west-2.elasticbeanstalk.com/'

    def get_request(self, resource):
        """Get request template."""
        uri = f"{self.destination}{resource}"
        response = requests.get(uri)
        return response

    def update_request(self, resource, params=None):
        """Patch request template."""
        uri = f"{self.destination}{resource}"
        response = requests.patch(uri, params)
        return response
