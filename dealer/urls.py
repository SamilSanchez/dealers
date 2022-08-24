from django.contrib import admin
from django.urls import path, include

from dealer import viewsets as views
from rest_framework.routers import DefaultRouter

# router = routers.SimpleRouter()
router = DefaultRouter()
router.register(r'dealers', views.DealerViewSet)
router.register(r'officials', views.OfficialViewSet)
router.register(r'high_dealer', views.AcceptDealerViewSet)
router.register(r'create_high_dealer', views.CreateAcceptDealerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]   