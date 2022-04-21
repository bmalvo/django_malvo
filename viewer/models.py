from django.db import models
from django.db.models import Model, CharField, ForeignKey, DO_NOTHING, IntegerField, DateField, TextField, DateTimeField


class Genre(Model):
    name = CharField(max_length=128)


class Movie(Model):
    title = CharField(max_length=128)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)
