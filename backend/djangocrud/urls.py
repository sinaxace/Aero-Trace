"""djangocrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from djangocrud.api import views
<<<<<<< HEAD

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'city', views.cityViewSet)
router.register(r'airline', views.airline_infoViewSet)
=======
from djangocrud.api.models import Airline,Movie,Country, City

router = routers.DefaultRouter()
router.register(r'Airline', views.BaseAirlineViewSet)
router.register(r'Movie', views.MovieViewSet)
router.register(r'Country', views.BaseCountryViewSet)
router.register(r'City', views.BaseCityViewSet)

>>>>>>> fe442b0f686bdc841b080e438f821a1f30c59595

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]