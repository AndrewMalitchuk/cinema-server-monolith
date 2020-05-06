from django import forms

from .models import *


class HallForm(forms.ModelForm):
    """
    A class that represents a form for Hall entity
    """

    class Meta:
        model = Hall
        fields = '__all__'


class CinemaForm(forms.ModelForm):
    """
    A class that represents a form for Cinema entity
    """

    class Meta:
        model = Cinema
        fields = '__all__'


class PosterForm(forms.ModelForm):
    """
    A class that represents a form for Poster entity
    """

    class Meta:
        model = Poster
        fields = '__all__'


class TimelineForm(forms.ModelForm):
    """
    A class that represents a form for Timeline entity
    """

    class Meta:
        model = Timeline
        fields = '__all__'
