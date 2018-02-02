from django.contrib import admin
from .models import Movie, Song


# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    pass


admin.site.register(Movie, MovieAdmin)
admin.site.register(Song, MovieAdmin)
