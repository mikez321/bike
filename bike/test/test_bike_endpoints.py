from rest_framework.test import APIClient
from django.test import TestCase
from bike.models import Bike
from IPython import embed

class BikeEndpointTest(TestCase):
    def setUp(self):
        """Create a bike to test and a client to make requests."""
        self.client = APIClient()
        self.bike = Bike.objects.create(
            make='Specialized',
            model='Chisel',
            type=2,
            description="It's a hardtail 29er.",
            f_axle=2,
            r_axle=2,
        )
        self.bike = Bike.objects.create(
            make='Fairdale',
            model='Goodship',
            type=1,
            description='A steel and carbon road bike.',
            f_axle=1,
            r_axle=1,
        )

    def test_bike_list(self):
        """GET request for all bikes."""
        response = self.client.get('/bikes/')
        self.assertEqual(response.status_code, 200)

        num_bikes = Bike.objects.all().count()
        self.assertEqual(len(response.data), num_bikes)
