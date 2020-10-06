from rest_framework import generics, filters
from movies.models import Movie
from movies.serializers import MoviesSerializer

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'year_of_release']


class MovieDetail(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer


