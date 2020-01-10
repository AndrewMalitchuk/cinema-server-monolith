from rest_framework import serializers

from .models import Film


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        # TODO: change fields
        # fields=('title', 'date', 'duration', 'genre')
        fields = '__all__'
