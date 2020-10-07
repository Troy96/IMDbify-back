from watchedlist.models import WatchedList
from watchlist.models import WatchList
from watchedlist.serializers import WatchedListSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.authentication import TokenAuthentication
from movies.models import Movie
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import exception_handler

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def view_or_add_to_watchedlist(request):

    if request.method == 'GET':
        data = request.user.watchedlist_set.all()
        serializer = WatchedListSerializer(data, many=True)
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
            watchlistobj.delete() #Delete the movie from watchlist if exists for a user
        except:
            pass
        try:
            watchedlistobj = WatchedList.objects.get(movie=movie, user=user)
            return JsonResponse({'detail': 'Movie already added in Watchlist!'}, status=400)
        except WatchedList.DoesNotExist:
            watchedlist = WatchedList()
            watchedlist.user = user
            watchedlist.movie = movie
            watchedlist.save()
            return JsonResponse({'detail': 'Movie added to Watchedlist!'}, status=201)




@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def remove_from_watchedlist(request, movieId):

    user = request.user

    try:
        movie = Movie.objects.get(id=movieId)
    except Movie.DoesNotExist:
        return JsonResponse({'detail': 'Movie does not exist'}, status=404)
    try:
        watchedlistobj = WatchedList.objects.get(user=user, movie=movie)
    except WatchedList.DoesNotExist:
        return JsonResponse({'detail': 'Movie not found in Watchedlist'}, status=404)

    watchedlistobj.delete()
    return JsonResponse({'detail': 'Movie removed from Watchedlist'}, status=204)







