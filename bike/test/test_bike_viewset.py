"""Test Bike Viewset."""

from rest_framework.test import APIClient
from django.test import TestCase
from bike.models import Bike


class BikeEndpointTest(TestCase):
    """Testing for CRUD endpoints of bikes."""

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
            brake_type=2,
            f_axle=1,
            r_axle=1,
        )

    def test_bike_list(self):
        """GET request for all bikes."""
        response = self.client.get('/bikes/')
        self.assertEqual(response.status_code, 200)

        num_bikes = Bike.objects.count()
        self.assertEqual(len(response.data), num_bikes)

    def test_bike_detail(self):
        """GET request for a single bike by pk."""
        response = self.client.get('/bikes/2/')
        self.assertEqual(response.status_code, 200)

        bike1 = Bike.objects.first()
        bike2 = Bike.objects.last()
        self.assertNotEqual(response.data['id'], bike1.id)
        self.assertEqual(response.data['id'], bike2.id)

    def test_bike_creation(self):
        """POST request to add a bike."""
        num_starting_bikes = Bike.objects.count()
        self.assertEqual(num_starting_bikes, 2)

        new_bike_attributes = {
            'make': 'Specialized',
            'model': 'Enduro',
            'type': 2,
            'description': 'Grip it and rip it',
            'f_axle': 2,
            'r_axle': 2,
        }
        response = self.client.post(
            '/bikes/', new_bike_attributes, format='json'
        )

        self.assertEqual(response.status_code, 201)
        current_num_bikes = Bike.objects.count()
        self.assertEqual(current_num_bikes, 3)

    def test_bike_update(self):
        """PATCH/PUT request to update a bike."""
        bike = Bike.objects.first()
        self.assertEqual(bike.description, "It's a hardtail 29er.")
        bike_updates = {
            'make': 'Specialized',
            'model': 'Chisel',
            'type': 2,
            'description': "It's all Flexy Jackson.",
            'f_axle': 2,
            'r_axle': 2,
        }
        response = self.client.patch(
            '/bikes/1/', bike_updates, format='json'
        )
        self.assertEqual(response.status_code, 200)
        updated_bike = Bike.objects.first()
        self.assertEqual(updated_bike.description, "It's all Flexy Jackson.")

    def test_bike_delete(self):
        """DELETE request for bikes."""
        num_starting_bikes = Bike.objects.count()
        self.assertEqual(num_starting_bikes, 2)

        response = self.client.delete('/bikes/1/')
        self.assertEqual(response.status_code, 204)
        updated_num_bikes = Bike.objects.count()
        self.assertEqual(updated_num_bikes, 1)
