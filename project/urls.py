"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dealer import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home_page"),
    path('api/', include('dealer.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('portal/dealer', views.DealerView.as_view(), name='create_dealer'),
    path('portal/dealers', views.DealerListView.as_view(), name='dealers_list'),
    path('portal/official', views.OfficialView.as_view(), name='create_dealers'),
    path('portal/officials', views.OfficialsListView.as_view(), name='officials_list'),
    path('portal_internal/high_dealer', views.HighDealerView.as_view(), name='high_dealer'),
    path('portal_internal/high_dealers', views.HighDealersView.as_view(), name='high_dealer'),
]
