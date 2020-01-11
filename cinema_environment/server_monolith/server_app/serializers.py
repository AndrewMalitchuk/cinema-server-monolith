from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from hashlib import md5

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

    def get_code(self):
        microsecond = datetime.now().microsecond
        return md5(str(microsecond).encode()).hexdigest()

    class Meta:
        model = Ticket
        # TODO: change fields
        # fields = ('id', 'place', 'status', 'cinema_id', 'film_id', 'user', 'code')
        fields = '__all__'

    def create(self, validated_data):
        place = validated_data.get('place')
        status = validated_data.get('status')
        cinema_id = validated_data.get('cinema_id')
        film_id = validated_data.get('film_id')
        user = validated_data.get('user')
        code = self.get_code()
        ticket = Ticket.objects.create(place=place, status=status, cinema_id=cinema_id, film_id=film_id, user=user,
                                       code=code)

        return ticket


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
        fields = ("id", "email", "password", "username", "is_staff")
