from contextlib import ContextDecorator
from dataclasses import dataclass, field
from math import radians
from typing import Dict
from urllib import parse
import requests

from django.conf import settings

class APIKeyError(Exception):
    pass

class GeoCacheApiWrapper(ContextDecorator):
    '''
    Context managed API Wrapper that provides interaction with Google's GeoCache API.
     Safely manages session, to be used with `with` clause.
    '''
    def __init__(self):
        self.safely_initialized = False
        self.base_url = 'https://maps.google.com/maps/api/geocode/json'
        try:
            self.api_key = settings.GEOCODING_API_KEY
        except:
            raise APIKeyError('GEOCODING_API_KEY not found in Environment variables.')

    def __enter__(self):
        self.session = requests.Session()
        self.session.params = {'key': self.api_key}
        return self

    def __exit__(self, type, value, traceback):
        self.session.close()

    def get_geocode(self, query: Dict[str, str]):
        '''
        Returns geocode response for given query

        Parameters:
        -----------
        query: Dict[str, str]
            Keys correspond to available keys from Geocache API

        Returns
        -------
        Dictionary of the API response
        '''
        if not query:
            raise ValueError('Expected query to be non-empty.')
        encoded_query = ''
        for key in query:
            encoded_query += f'{parse.quote_plus(key)}={parse.quote_plus(query[key])}'
        query_url = f'{self.base_url}?{encoded_query}&key={self.api_key}'
        return self.session.get(query_url).json()

class LatLongCoordinate(object):
    '''
    Represents a coordinate in latitude, longitude format.
    '''
    def __init__(self, coordinate_as_str: str):
        '''
        Takes and input coordinate in string format and generates a LatLongCoordinate object.

        Parameters
        ----------
        coordinate_as_str: str
            Expected format example: 40.714224,-73.961452
        '''
        self.coordinate_as_str = coordinate_as_str
        coordinates = coordinate_as_str.split(',')
        self.latitude = float(coordinates[0])
        self.longitude = float(coordinates[1])
        self.latitute_radians = radians(self.latitude)
        self.longitude_radians = radians(self.longitude)
