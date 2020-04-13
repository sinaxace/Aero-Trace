from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import MovieSerializer,MovieMiniSerializer,Airline,BaseAirlineSerializer,BaseCountrySerializer,BaseCitySerializer
from .models import Movie,Airline,Country,City
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest.arrival import Arrivial

from . import serializers
from . import Task
import requests
import json



class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    # This is a built-in function returns only id and title of the Movies in order to send it faster.
    def list(self, request, *args, **kwargs):
        movies = ApiMovie.objects.all()
        seralizer = MovieMiniSerializer(movies, many=True)
        return Response(seralizer.data)

    
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
#Get arrival flight api from Toronto Pearson 
todayArr = requests.get("https://gtaa-fl-prod.azureedge.net/api/flights/list?type=ARR&day=today&useScheduleTimeOnly=false")
#tomorrowArr = requests.get("https://gtaa-fl-prod.azureedge.net/api/flights/list?type=ARR&day=tomorrow&useScheduleTimeOnly=false")
#Get file path
parsed = json.loads(todayArr.text)
schedule = parsed['list']

#Get flight id
id_list = []
country_list = []

for id_ in schedule:
      id_list.extend((id_["al"], id_['id2'], id_["schTime"][:10], id_["gate"], id_["term"], id_["routes"][0]["name"]))
      country_list.append(id_["routes"][0]["cnty"])

print('-------country_list------')
print(country_list)

dic = {}
#Create country first
for country in schedule:
    for c in country_list:
        dic[c] = []
print('-------dic[c]------')
print(dic) 

#Create country list
countries = []
for country in country_list:
    if not country in countries:
        countries.append(country)
print('-------countries------')
print(countries)

    


def adding_city(schedule, dic):

    for s in schedule:
        if s["routes"][0]["cnty"] in dic:
            if s["routes"][0]["city"] not in dic[s["routes"][0]["cnty"]]:
                dic[s["routes"][0]["cnty"]].append(s["routes"][0]["city"])
    return dic

city_country_list = adding_city(schedule,dic)
print('-------city_country_list------')
print(city_country_list)

#Genertate new country city json format
arrivalCity = {}
def arrival_coutry_city(schedule,dic):
    arrivalCity["arrivalCity"] = []
    for country in city_country_list1          :

        
arrivalCity["arrivalCity"] = []
# arrivalCity["arrivalCity"].append({"Country":"CAN","City":[]})
# arrivalCity["arrivalCity"].append({"Country":"CAN","City":["a"]})
# arrivalCity["arrivalCity"]["Country"].append({"City":"b"})

# arrivalCity["arrivalCity"].append({"Country":"USA"})

# arrivalCity["arrivalCity"]["Country"].append({""})
# arrivalCity["arrivalCity"]["Country"] = 'USA'

# arrivalCity["arrivalCity"].append({"Country":"CAN","City":["a","b"]})

print('-------arrivalCity------')
print(arrivalCity)    



class TaskViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
     def list(self, request):
        return Response(city_country_list)

    

# class TaskViewSet(viewsets.ViewSet):
#     # Required for the Browsable API renderer to have a nice form.
#     serializer_class = serializers.TaskSerializer

#     def list(self, request):
#         serializer = serializers.TaskSerializ)
#         return Response(serializer.data)