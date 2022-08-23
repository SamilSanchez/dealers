from django.contrib import admin
from django.urls import path, include

from dealer import viewsets as views
from rest_framework import routers, viewsets

router = routers.SimpleRouter()
router.register(r'dealers', views.DealerViewSet)
router.register(r'officials', views.OfficialViewSet)
router.register(r'high_dealer', views.AcceptDealerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]   