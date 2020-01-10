from rest_framework import serializers

from .models import Film, Cinema, Timeline, Poster, Hall, Ticket


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        # TODO: change fields
        # fields=('title', 'date', 'duration', 'genre')
        fields = '__all__'


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        # TODO: change fields
        fields = '__all__'


class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        # TODO: change fields
        fields = '__all__'


class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = '__all__'


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        # TODO: change fields
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        # TODO: change fields
        fields = '__all__'
