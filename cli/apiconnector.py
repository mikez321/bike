"""A single module to interact with the API."""

import requests


class ApiConnector():
    """Reusable module allowing connection to the bike API."""

    destination = 'http://localhost:8000/'

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
