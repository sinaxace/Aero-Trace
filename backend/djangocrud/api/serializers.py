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
        fields = ['city_id', 'city_name', 'country_id']

#TODO: Change the name of the Task and Movie functions to FLight related names.

class TaskSerializer(serializers.Serializer):
     id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=256)
    # owner = serializers.CharField(max_length=256)
    # status = serializers.ChoiceField(choices=STATUSES, default='New')

    # def create(self, validated_data):
    #     return Task(id=None, **validated_data)

    # def update(self, instance, validated_data):
    #     for field, value in validated_data.items():
    #         setattr(instance, field, value)
    #     return instance

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email','password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user