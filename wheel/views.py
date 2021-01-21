from django.shortcuts import render, get_object_or_404
from wheel.models import FrontWheel, RearWheel
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from itertools import chain
from wheel.serializers import (FrontWheelSerializer,
                               RearWheelSerializer,
                               GenericWheelSerializer)


class WheelList(APIView):
    """Hand Rolled list view for all wheels."""

    def get(self, request, format=None):
        """GET list of all wheels regardless of F or R."""
        f_wheels = FrontWheel.objects.all()
        r_wheels = RearWheel.objects.all()
        all_wheels = chain(f_wheels, r_wheels)
        serializer = GenericWheelSerializer(all_wheels, many=True)
        return Response(serializer.data)


class FrontWheelViewSet(viewsets.ViewSet):
    """Viewset for wheel detail and wheel list."""

    def list(self, request):
        """List all front wheels in the database."""
        queryset = FrontWheel.objects.all()
        serializer = FrontWheelSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Return a single front wheel by pk."""
        queryset = FrontWheel.objects.all()
        f_wheel = get_object_or_404(queryset, pk=pk)
        serializer = FrontWheelSerializer(f_wheel)
        return Response(serializer.data)


class RearWheelViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset for wheel detail and wheel list."""

    queryset = RearWheel.objects.all()
    serializer_class = RearWheelSerializer
