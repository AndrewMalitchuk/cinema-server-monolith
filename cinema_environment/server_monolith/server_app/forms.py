from django import forms

from .models import *


class HallForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = '__all__'


class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = '__all__'

class PosterForm(forms.ModelForm):
    class Meta:
        model = Poster
        fields = '__all__'

class TimelineForm(forms.ModelForm):
    class Meta:
        model = Timeline
        fields = '__all__'

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'