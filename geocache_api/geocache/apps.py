from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class GeoCacheConfig(AppConfig):
    name = "geocache_api.geocache"
    verbose_name = _("GeoCache")