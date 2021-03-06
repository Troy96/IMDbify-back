from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from users.serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create(request):
    data = JSONParser().parse(request)
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)



