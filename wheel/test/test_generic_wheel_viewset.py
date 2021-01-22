"""Generic wheel list endpoint test."""


from rest_framework.test import APIClient
from django.test import TestCase
from wheel.models import RearWheel, FrontWheel


class GenericWheelEndpointTest(TestCase):
    """Tests for all wheel list endpoint /wheels/."""

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
        self.wheel3 = FrontWheel.objects.create(
            manufacturer='DT Swiss',
            model='350',
            material=2,
        )
        self.wheel4 = FrontWheel.objects.create(
            manufacturer='Zipp',
            model='404',
            axle=1,
            material=1,
        )

    def test_rearwheel_list(self):
        """GET request for all rear wheels."""
        response = self.client.get('/wheels/')
        self.assertEqual(response.status_code, 200)

        num_rear_wheels = RearWheel.objects.count()
        num_front_wheels = FrontWheel.objects.count()
        num_wheels = num_rear_wheels + num_front_wheels
        self.assertEqual(len(response.data), num_wheels)

        response_models = []
        for wheel in response.data:
            response_models.append(wheel['model'])

        db_models = [
            self.wheel1.model,
            self.wheel2.model,
            self.wheel3.model,
            self.wheel4.model,
        ]

        self.assertEqual(set(db_models), set(response_models))
