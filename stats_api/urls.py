from django.urls import path, register_converter
from .views import FortniteStats
from .converters import PlatformTypeConverter

register_converter(PlatformTypeConverter, 'plat')


urlpatterns = [
    path('<plat:platform>/<user>/',FortniteStats.as_view(), name='plat'),
]