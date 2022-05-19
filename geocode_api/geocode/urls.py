from django.urls import path

from geocode_api.geocode.apis import (
    GeocodeBaseApi,
    AddressSearchApi,
    CoordinateCalculateApi
)

app_name = 'geocode'
urlpatterns = [
    path('search/', AddressSearchApi.as_view(), name='search'),
    path('distance/', CoordinateCalculateApi.as_view(), name='distance'),
    path('', GeocodeBaseApi.as_view(), name='geocode')
]
