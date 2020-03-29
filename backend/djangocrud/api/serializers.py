from django.contrib.auth.models import User
from rest_framework import serializers
<<<<<<< HEAD
<<<<<<< HEAD
from .models import ApiMovie, City, AirlineInfo
=======

=======
from rest_framework import status
>>>>>>> origin/merge
from .models import Movie,Airline,Country,City
>>>>>>> fe442b0f686bdc841b080e438f821a1f30c59595

from . import Task



class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'desc', 'year']


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
        fields = ['city_id', 'city_name', 'country_id']

STATUSES = (
    'New',
    'Ongoing',
    'Done',
)


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=256)
    owner = serializers.CharField(max_length=256)
    status = serializers.ChoiceField(choices=STATUSES, default='New')

    def create(self, validated_data):
        return Task(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance

