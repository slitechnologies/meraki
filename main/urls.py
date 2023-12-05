from django.urls import path
from main.views import MerakiProxyView

urlpatterns = [
     path('api/meraki/<path:path>', MerakiProxyView.as_view(), name='meraki-proxy'),
]
