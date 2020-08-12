from django.db import models
from users.models import User

class MyCollection(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField()
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    movies =  models.ManyToManyField(Movie)

    class Meta:
        ordering = ['created']

    def get_movies(self):
        return ""