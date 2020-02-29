from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import MovieSerializer,MovieMiniSerializer
from .models import Movie
from rest_framework.response import Response

class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    # This is a built-in function returns only id and title of the Movies in order to send it faster.
    def list(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        seralizer = MovieMiniSerializer(movies, many=True)
        return Response(seralizer.data)