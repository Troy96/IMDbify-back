from watchlist.models import WatchList
from watchlist.serializers import WatchListSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.authentication import TokenAuthentication
from movies.models import Movie
from rest_framework.decorators import api_view, authentication_classes, permission_classes

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def view_or_add_to_watchlist(request):

    if request.method == 'GET':
        data = request.user.watchlist_set.all()
        serializer = WatchListSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        user = request.user
        movieId = JSONParser().parse(request)['movie']

        try:
            movie = Movie.objects.get(id=movieId)
        except Movie.DoesNotExist:
            return  JsonResponse({'detail': 'Movie not found'}, status=404)

        try:
            watchlistobj = WatchList.objects.get(movie=movie, user=user)
            return  JsonResponse({'detail': 'Movie already added in watchlist!'}, status=400)
        except WatchList.DoesNotExist:
            watchlist = WatchList()
            watchlist.user = user
            watchlist.movie = movie
            watchlist.save()
            return  JsonResponse({'detail': 'Movie  added in watchlist!'}, status=201)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def remove_from_watchlist(request, movieId):

    user = request.user

    try:
        movie = Movie.objects.get(id=movieId)
    except Movie.DoesNotExist:
        return JsonResponse({'detail': 'Movie does not exist'}, status=404)
    try:
        watchlistobj = WatchList.objects.get(user=user, movie=movie)
    except WatchList.DoesNotExist:
        return JsonResponse({'detail': 'Movie not found in Watchlist'}, status=404)

    watchlistobj.delete()
    return JsonResponse({'detail': 'Movie removed from Watchlist'}, status=204)







