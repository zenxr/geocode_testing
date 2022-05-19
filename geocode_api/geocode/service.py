import json
from math import asin, cos, sin, sqrt

from geocode_api.geocode.geocode_classes import GeocodeApiWrapper, LatLongCoordinate
from geocode_api.users.models import User

EARTH_RADIUS_MILES = 3959.87433
EARTH_RADIUS_KILOMETERS = 6372.8

class InvalidGeocodeApiResponse(Exception):
    pass

def search_address(address: str):
    '''
    Given an input address query, returns the best matching full address
     and latitude,longitude coordinates for the address.

    Parameters:
    -----------
    address: str
        Expected format: 1111 Googleway Drive, Somewhere USA

    Returns
    -------
    dict
        Dictionary with keys of `formatted_address` and `location`
    '''
    if not address:
        raise ValueError('Address cannot be empty')
    with GeocodeApiWrapper() as geo_api:
        response = geo_api.get_geocode({'address': address})
        if response['status'] != 'OK':
            return response
        try:
            return {'formatted_address' : response['results'][0]['formatted_address'],
                'location' : response['results'][0]['geometry']['location']
            }
        except Exception as e:
            raise InvalidGeocodeApiResponse('Google Geocode API response format did not match expected')

def get_distance_between(start_coord: str, end_coord: str, user: User):
    '''
    Returns distance between two latitude, longitude coordinates using Haversine formula. Each coordinate input is a string.
    
    Parameters
    ----------
    start_coord: str
        Expected format example: 40.714224,-73.961452
    end_coord: str
        Expected format example: 40.714224,-73.961452

    Returns
    -------
    dict
        Dictionary with keys of `distance` and `units`
    '''
    if user.prefer_metric:
        radius = EARTH_RADIUS_KILOMETERS
        units = 'kilometers'
    else:
        radius = EARTH_RADIUS_MILES
        units = 'miles'
    start = LatLongCoordinate(start_coord)
    end = LatLongCoordinate(end_coord)
    lat_distance = start.latitute_radians - end.latitute_radians
    long_distance = start.longitude_radians - end.longitude_radians
    a = sin(lat_distance / 2)**2 + cos(start.latitute_radians) * cos(end.latitute_radians) * sin(long_distance / 2)**2
    c = 2 * asin(sqrt(a))
    distance = c * radius
    return {'distance': distance, 'units': units}
