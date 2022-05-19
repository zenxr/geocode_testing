from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class GeocodeConfig(AppConfig):
    name = "geocode_api.geocode"
    verbose_name = _("Geocode")