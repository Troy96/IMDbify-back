from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie

class WatchedList(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)