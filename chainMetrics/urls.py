from django.urls import path
from .views import chainMetrics


urlpatterns = [
     path('chain-metrics/', chainMetrics, name='chain-metrics'),
]
