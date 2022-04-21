from django.contrib import admin
from django.urls import path

from viewer.models import Genre, Movie
from viewer.views import hello

admin.site.register(Genre)
admin.site.register(Movie)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<s>', hello)
]
