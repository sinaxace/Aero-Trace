from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import MovieSerializer,MovieMiniSerializer,cityMiniSerializer,citySerializer,airline_infoSerializer,airline_infoMiniSerializer
from .models import ApiMovie, City,AirlineInfo
from rest_framework.response import Response

class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ApiMovie.objects.all()
    serializer_class = MovieSerializer

    # This is a built-in function returns only id and title of the Movies in order to send it faster.
    def list(self, request, *args, **kwargs):
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
