import uuid
from django.db import models
from django.conf import settings
from moviesite.movies.models import Movie

class MyCollection(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField()
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movies =  models.ManyToManyField(Movie)

    def get_movies(self):
        return ""