from django.contrib.auth.models import User
from rest_framework import serializers
<<<<<<< HEAD
from .models import ApiMovie, City, AirlineInfo
=======

from .models import Movie,Airline,Country,City
>>>>>>> fe442b0f686bdc841b080e438f821a1f30c59595


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
<<<<<<< HEAD
        model = ApiMovie
=======
        model = Movie
>>>>>>> fe442b0f686bdc841b080e438f821a1f30c59595
        fields = ['id', 'title', 'desc', 'year']

class MovieMiniSerializer(serializers.ModelSerializer):
    class Meta:
<<<<<<< HEAD
        model = ApiMovie
        fields = ['id', 'title']

class citySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'city_id', 'city_name']
        
class cityMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'city_id']

class airline_infoSerializer(serializers.ModelSerializer):
    class Meta:
            model = AirlineInfo
            fields = ['airline_info_id', 'airline_id', 'terminal_id','counter_loaction_id','route_id','contact_no','website']

class airline_infoMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirlineInfo
        fields = ['airline_info_id', 'airline_id']

=======
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
>>>>>>> fe442b0f686bdc841b080e438f821a1f30c59595
