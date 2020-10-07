from django.db import models

class Movie(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, blank=True, default='')
    image = models.CharField(max_length=100, blank=True, default='')
    year_of_release = models.IntegerField(blank=True, null=True)
    director = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        ordering = ['created']

