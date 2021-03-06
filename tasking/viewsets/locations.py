# -*- coding: utf-8 -*-
"""
Location viewsets
"""
from __future__ import unicode_literals

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from tasking.models import Location
from tasking.serializers import LocationSerializer


# pylint: disable=too-many-ancestors
class LocationViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                      mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                      mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    Viewset for Location
    """
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter]
    filter_fields = ['parent', 'country']
    search_fields = ['name']
    ordering_fields = ['name', 'created']
    queryset = Location.objects.all()
