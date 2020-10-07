from watchlist.models import WatchList
from watchlist.serializers import WatchListSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.authentication import TokenAuthentication
from movies.models import Movie
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, authentication_classes, permission_classes

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def view_or_create_watchlist(request):

    if request.method == 'GET':
        data = WatchList.objects.filter(user__email=request.user.email)
        serializer = WatchListSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        user = request.user
        movieId = JSONParser().parse(request)['movie']
        movie = Movie.objects.get(id=movieId)

        watchlist = WatchList()
        watchlist['user'] = user
        watchlist['movie'] = movie
        watchlist.save()
        return HttpResponse(status=201)



