from django.contrib.auth.models import User
from rest_framework import viewsets
<<<<<<< HEAD
from .serializers import MovieSerializer,MovieMiniSerializer,cityMiniSerializer,citySerializer,airline_infoSerializer,airline_infoMiniSerializer
from .models import ApiMovie, City,AirlineInfo
=======
from .serializers import MovieSerializer,MovieMiniSerializer,Airline,BaseAirlineSerializer,BaseCountrySerializer,BaseCitySerializer
from .models import Movie,Airline,Country,City
>>>>>>> fe442b0f686bdc841b080e438f821a1f30c59595
from rest_framework.response import Response

class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
<<<<<<< HEAD
    queryset = ApiMovie.objects.all()
=======
    queryset = Movie.objects.all()
>>>>>>> fe442b0f686bdc841b080e438f821a1f30c59595
    serializer_class = MovieSerializer

    # This is a built-in function returns only id and title of the Movies in order to send it faster.
    def list(self, request, *args, **kwargs):
<<<<<<< HEAD
        movies = ApiMovie.objects.all()
        seralizer = MovieMiniSerializer(movies, many=True)
        return Response(seralizer.data)

class cityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = City.objects.all()
    serializer_class = citySerializer

    # This is a built-in function returns only id and title of the Movies in order to send it faster.
    def list(self, request, *args, **kwargs):
        movies = City.objects.all()
        seralizer = cityMiniSerializer(movies, many=True)
        return Response(seralizer.data)

class airline_infoViewSet(viewsets.ModelViewSet):
    queryset = AirlineInfo.objects.all()
    serializer_class = airline_infoSerializer

    def list(self, request, *args, **kwargs):
        airlineinfo = AirlineInfo.objects.all()
        serializer = airline_infoMiniSerializer(airlineinfo, many=True)
        return Response(serializer.data)
=======
        movies = Movie.objects.all()
        seralizer = MovieMiniSerializer(movies, many=True)
        return Response(seralizer.data)
    
class BaseAirlineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Airline.objects.all()
    serializer_class = BaseAirlineSerializer

    # 
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
>>>>>>> fe442b0f686bdc841b080e438f821a1f30c59595
