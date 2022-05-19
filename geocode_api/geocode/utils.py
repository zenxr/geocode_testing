from rest_framework.serializers import ValidationError

def lat_long_validator(coordinates: str):
    """
    Validates a given string matches coordinate format.

    Expected format example: 40.714224,-73.961452
    """
    split_coords = coordinates.split(',')
    if len(split_coords) != 2:
        raise ValidationError(f'Latitude Longitude format incorrect: {coordinates}')
    latitude, longitude = split_coords
    try:
        latitude, longitude = float(latitude), float(longitude)
    except ValueError:
        raise ValidationError(f'Latitude Longitude format incorrect: {coordinates}')