from django import forms

from .models import Cinema, Hall, Film


class HallForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = '__all__'


class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = '__all__'

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'