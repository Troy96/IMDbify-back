from django.db import models

class Movie(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, default='')
    image = models.CharField(max_length=100, default=''),
    year_of_release = models.IntegerField(),
    director = models.CharField(max_length=50, default='')

    class Meta:
        ordering = ['created']

