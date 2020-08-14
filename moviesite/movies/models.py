from django.db import models

# Create your models here.

# Create your models here.
class Genre(models.Model):
    """
    Genre model : Table for movie Genres
    """
    name = models.CharField(max_length=500)
    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
    def __str__(self):
        return self.name
    

class Movie(models.Model):
    """
    Movie model : model for Movies
    """
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    genres = models.CharField(max_length=500)
    uuid = models.UUIDField()
    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
    def __str__(self):
        return self.title