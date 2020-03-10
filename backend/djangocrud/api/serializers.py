from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ApiMovie, City, AirlineInfo


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiMovie
        fields = ['id', 'title', 'desc', 'year']

class MovieMiniSerializer(serializers.ModelSerializer):
    class Meta:
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

