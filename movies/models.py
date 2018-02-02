from django.db import models


# Create your models here.
class Movie(models.Model):
    movie = models.CharField(max_length=255)
    actor = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)

    def __str__(self):
        return self.movie


class Song(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='songs')
    name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=255)

    def __str__(self):
        return self.name
