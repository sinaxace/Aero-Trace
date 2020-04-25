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

from djangocrud.api.models import Airline, Country, City
from djangocrud.api.views import TaskViewSet
from djangocrud.api.views import Country_City_List_Dep



## TODO:
### Create move all the paths for djangocrud/api applications to the api/urls.py class
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'Airline', views.BaseAirlineViewSet)
router.register(r'Country', views.BaseCountryViewSet)
router.register(r'City', views.BaseCityViewSet)
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'Dep_Country_City_list', Country_City_List_Dep, basename='Dep_Country_City_list')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]