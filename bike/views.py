"""Bike viewSets offer full CRUD functionality for bikes."""
from rest_framework import viewsets
from bike.models import Bike
from bike.serializers import BikeSerializer


class BikeViewSet(viewsets.ModelViewSet):
    """API viewset offering full CRUD for bike model."""

    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
