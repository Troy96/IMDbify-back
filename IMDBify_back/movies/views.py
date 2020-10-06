from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from movies.models import Movie
from movies.serializers import MoviesSerializer

def movie_list(request):
    '''
    List out all the movies with details
    :param request:
    :return:
    '''
    movies = Movie.objects.all()
    serializer = MoviesSerializer(movies, many=True)
    return JsonResponse(serializer.data, safe=False)


def movie_detail(request, pk):
    '''
    Returns a single movie with detail
    :param request:
    :return:
    '''
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return HttpResponse(status=404)

    serializer = MoviesSerializer(movie)
    return JsonResponse(serializer.data)


