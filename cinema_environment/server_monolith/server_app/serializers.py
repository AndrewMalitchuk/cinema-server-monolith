from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

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


UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    # Тут в ...objects.create(..)  можеш додати ті поля які треба передати
    # і додай їх в Мету
    # і прошу тебе, Андрей, зоть деколи дивись що ти робиш
    # username обезательно бо воно юнік (хз крч)
    def create(self, validated_data):
        user = UserModel.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            is_staff=validated_data['is_staff'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = UserModel
        fields = ("id", "email", "password","username","is_staff")
