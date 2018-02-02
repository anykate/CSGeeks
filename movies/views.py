from django.shortcuts import render, redirect
from .models import Movie


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def details(request, movie_id):
    # print(movie_id)
    try:
        movie = Movie.objects.get(id=movie_id)
        songs = movie.songs.all()

    except Movie.DoesNotExist:
        return redirect('/')

    return render(request, 'movies/details.html', {'songs': songs, 'movie': movie})
