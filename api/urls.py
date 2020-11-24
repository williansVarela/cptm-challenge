from django.conf.urls import url, include
from django.urls import path, include
from rest_framework import routers
from api.controllers import drone


router = routers.DefaultRouter()
router.register(r'rails', drone.RailsViewSet)
router.register(r'electricalnetwork', drone.ElectricalNetworkViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api/", include('rest_framework.urls')),
]
