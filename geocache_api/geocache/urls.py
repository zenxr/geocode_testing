from django.urls import path

from geocache_api.geocache.apis import (
    GeoCacheBaseApi,
    AddressSearchApi,
    CoordinateCalculateApi
)

app_name = 'geocache'
urlpatterns = [
    path('search/', AddressSearchApi.as_view(), name='search'),
    path('distance/', CoordinateCalculateApi.as_view(), name='distance'),
    path('', GeoCacheBaseApi.as_view(), name='geocache')
]
