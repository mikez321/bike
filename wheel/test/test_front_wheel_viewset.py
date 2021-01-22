"""FrontWheel endpoint tests."""

from rest_framework.test import APIClient
from django.test import TestCase
from wheel.models import FrontWheel


class FrontWheelEndpointTest(TestCase):
    """Tests for FrontWheel endpoints."""

    def setUp(self):
        """Create wheels to test and a client to make requests."""
        self.client = APIClient()
        self.wheel1 = FrontWheel.objects.create(
            manufacturer='DT Swiss',
            model='240s',
            material=2,
        )
        self.wheel2 = FrontWheel.objects.create(
            manufacturer='Zipp',
            model='404',
            axle=1,
            material=1,
        )

    def test_frontwheel_list(self):
        """GET request for all front wheels."""
        response = self.client.get('/wheels/front/')
        self.assertEqual(response.status_code, 200)

        num_wheels = FrontWheel.objects.count()
        self.assertEqual(len(response.data), num_wheels)

    def test_bike_detail(self):
        """GET request for a single bike by pk."""
        response = self.client.get(f'/wheels/front/{self.wheel1.id}/')
        self.assertEqual(response.status_code, 200)

        wheel1 = FrontWheel.objects.first()
        wheel2 = FrontWheel.objects.last()
        self.assertNotEqual(response.data['id'], wheel2.id)
        self.assertEqual(response.data['id'], wheel1.id)
