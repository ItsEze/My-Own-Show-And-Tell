from django.urls import path
from .views import FortniteStore

urlpatterns = [
    path('',FortniteStore.as_view())
]