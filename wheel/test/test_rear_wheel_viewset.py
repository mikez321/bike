"""RearWheel endpoint tests."""

from rest_framework.test import APIClient
from django.test import TestCase
from wheel.models import RearWheel


class RearWheelEndpointTest(TestCase):
    """Testing for RearWheel endpionts/viewsets."""

    def setUp(self):
        """Create wheels to test and a client to make requests."""
        self.client = APIClient()
        self.wheel1 = RearWheel.objects.create(
            manufacturer='DT Swiss',
            model='240s',
            material=2,
            driver=2,
        )
        self.wheel2 = RearWheel.objects.create(
            manufacturer='Enve',
            model='M3',
            axle=2,
            material=1,
            driver=2,
        )

    def test_rearwheel_list(self):
        """GET request for all rear wheels."""
        response = self.client.get('/wheels/rear/')
        self.assertEqual(response.status_code, 200)

        num_wheels = RearWheel.objects.count()
        self.assertEqual(len(response.data), num_wheels)

    def test_bike_detail(self):
        """GET request for a single bike by pk."""
        response = self.client.get(f'/wheels/rear/{self.wheel1.id}/')
        self.assertEqual(response.status_code, 200)

        wheel1 = RearWheel.objects.first()
        wheel2 = RearWheel.objects.last()
        self.assertNotEqual(response.data['id'], wheel2.id)
        self.assertEqual(response.data['id'], wheel1.id)
