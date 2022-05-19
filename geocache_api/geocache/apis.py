from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView

from geocache_api.geocache import service
from geocache_api.geocache.utils import lat_long_validator


class GeoCacheBaseApi(APIView, LoginRequiredMixin):
    def get(self, request):
        return Response(data={
            'search': reverse('geocache:search', request=request),
            'distance': reverse('geocache:distance', request=request)
        }, status=status.HTTP_200_OK)

class AddressSearchApi(APIView, LoginRequiredMixin):
    def get(self, request):
        address = request.GET.get('address', '')
        if not address or not isinstance(address, str):
            raise ValidationError('Address is a required field, must be urlencoded string in request parameter.')
        result = service.search_address(address)
        return Response(data=result, status=status.HTTP_200_OK)

class CoordinateCalculateApi(APIView, LoginRequiredMixin):
    def get(self, request):
        start = request.GET.get('start', '')
        end = request.GET.get('end', '')
        lat_long_validator(start)
        lat_long_validator(end)

        response = service.get_distance_between(
            start_coord = start,
            end_coord = end,
            user = request.user
        )
        return Response(response, status=status.HTTP_200_OK)

