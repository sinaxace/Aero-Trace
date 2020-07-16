from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Movie, Airline, Country, City, Restaurant, RestaurantRating


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

# TODO: Change the name of the Task and Movie functions to FLight related names.


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('restaurant_name', 'before_security', 'cusine_type',
                  'terminal', 'description', 'no_of_ratings', 'avg_rating')


class RestaurantRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantRating
        fields = ('restaurant', 'user', 'star', 'comment')
