from rest_framework import generics, filters
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from movies.models import Movie
from movies.serializers import MoviesSerializer
from .scraper import scrape
from datetime import datetime

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'year_of_release']


class MovieDetail(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer

def scrape_data(request):
    url_to_scrap = request.GET.get('url', '')
    data = scrape(url_to_scrap)
    for index in range(0, len(data)):
        scraped_movie = data[index]
        try:
            movie_obj = Movie.objects.get(name=scraped_movie['name'])
            movie_obj.updated = datetime.now()
            if movie_obj.image != scraped_movie['image']:
                movie_obj.image = scraped_movie['image']
            movie_obj.save()

        except Movie.DoesNotExist:
            movie = Movie()
            movie.name = scraped_movie['name']
            movie.image = scraped_movie['image']
            movie.year_of_release = scraped_movie['year_of_release']
            movie.director = scraped_movie['director']
            movie.save()

    return JsonResponse({'detail': 'Scraping completed successfully'}, status=201)



