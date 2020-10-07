from rest_framework import serializers
from watchedlist.models import WatchedList


class WatchedListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchedList
        fields = '__all__'