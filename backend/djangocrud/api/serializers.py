from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Movie,Airline,Country,City


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'desc', 'year']

class MovieMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title']


class BaseAirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ['airline_id', 'airline_name', 'airline_iata', 'airline_icao']

class BaseCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_id', 'country_name']

class BaseCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_id','city_name','country_id']