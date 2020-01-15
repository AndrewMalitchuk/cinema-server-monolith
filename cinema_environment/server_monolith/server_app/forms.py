from django import forms

from .models import Cinema, Hall


class HallForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = '__all__'


class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = '__all__'
