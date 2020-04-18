from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import UserSerializer,MovieSerializer, MovieMiniSerializer, Airline, BaseAirlineSerializer, BaseCountrySerializer,BaseCitySerializer
from .models import Airline,Country,City
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status
from rest.arrival import Arrivial

from . import serializers
# from . import Task
import requests
import json




    
class BaseAirlineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Airline.objects.all()
    serializer_class = BaseAirlineSerializer

    def list(self, request, *args, **kwargs):
        airlines = Airline.objects.all()
        seralizer = BaseAirlineSerializer(airlines, many=True)
        return Response(seralizer.data)

class BaseCountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Country.objects.all()
    serializer_class = BaseCountrySerializer

    # 
    def list(self, request, *args, **kwargs):
        countries = Country.objects.all()
        seralizer = BaseCountrySerializer(countries, many=True)
        return Response(seralizer.data)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class BaseCityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = City.objects.all()
    serializer_class = BaseCitySerializer

    # 
    def list(self, request, *args, **kwargs):
        cities = City.objects.all()
        seralizer = BaseCitySerializer(cities, many=True)
        return Response(seralizer.data)



class TaskViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
     def list(self, request):
        return Response(Arrivial.adding_city(Arrivial.schedule,Arrivial.dic))

    

# class TaskViewSet(viewsets.ViewSet):
#     # Required for the Browsable API renderer to have a nice form.
#     serializer_class = serializers.TaskSerializer

#     def list(self, request):
#         serializer = serializers.TaskSerializ)
#         return Response(serializer.data)