from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, action
from .serializers import UserSerializer, MovieSerializer, MovieMiniSerializer, Airline, BaseAirlineSerializer, BaseCountrySerializer, BaseCitySerializer, RestaurantSerializer, RestaurantRatingSerializer
from .models import Airline, Country, City, RestaurantRating, Restaurant
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status
from rest.arrival import Arrivial
from rest.departure import Departure
from rest.result import depResult
from rest.Restaurant import RestaurantAPI

from . import serializers
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
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(
            request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        serializer = UserSerializer(user, many=False)
        return Response({'token': token.key, 'user': serializer.data})


class BaseCityViewSet(viewsets.ViewSet):
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
        return Response(Arrivial.adding_city(Arrivial.schedule, Arrivial.dic))


class Country_City_List_Dep(viewsets.ViewSet):
    def list(self, request):
        return Response(Departure.adding_city_dep(Departure.schedule_dep, Departure.dic_country_city_dep_list))


class Dep_Flight_Schedule(viewsets.ViewSet):
    def list(self, request):
        return Response(depResult.dep_flight_schedule(depResult.schedule_dep))


class Resturant_List(viewsets.ViewSet):
    def list(self, request):
        return Response(RestaurantAPI.Restaurants)


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    @action(detail=True, methods=['POST'])
    def rate_restaurant(self, request, pk=None):
        if 'star' in request.data:
            restaurant = Restaurant.objects.get(id=pk)
            star = request.data['star']
            user = request.user
            print(user)
            print('Restaurant is '.format(restaurant.restaurant_name))

            try:
                rating = RestaurantRating.objects.get(
                    user=user.id, Restaurant=restaurant, star=star)
                rating.star = star
                rating.save()
                serializer = RestaurantRatingSerializer(rating, many=False)
                response = {
                    'message': 'Restaurant rating updated', 'result': serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = RestaurantRating.objects.create(
                    user=user.id, Restaurant=restaurant, start=star)
                serializer = RestaurantRatingSerializer(rating, many=False)
                response = {
                    'message': 'Restaurant rating created', 'result': serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response('Need to provide star', status=status.HTTP_400_BAD_REQUEST)


class RestaurantRatingViewSet(viewsets.ModelViewSet):
    def list(self, request):
        return Response(RestaurantAPI.Restaurants)
