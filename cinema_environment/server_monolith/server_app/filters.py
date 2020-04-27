import django_filters
from .models import *

class FilmFilter(django_filters.FilterSet):
    class Meta:
        model = Film
        fields = ['title', 'date', 'duration']