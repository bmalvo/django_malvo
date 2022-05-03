from django.shortcuts import render
from django.views import View
from django.views.generic import FormView

from viewer.forms import MovieForm
from viewer.models import Movie


class MoviesView(View):
    def get(self, request):
        return render(request, template_name='movies.html',
                  context={'movies': Movie.objects.all()})


class MovieCreateView(FormView):
    template_name = 'form.html'
    form_class = MovieForm

