from datetime import datetime
from hashlib import md5

from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Film, Cinema, Timeline, Poster, Hall, Ticket, Staff


class FilmSerializer(serializers.ModelSerializer):
    """
    Serializer for Film entity
    """

    class Meta:
        model = Film
        fields = '__all__'


class CinemaSerializer(serializers.ModelSerializer):
    """
    Serializer for Cinema entity
    """

    class Meta:
        model = Cinema
        fields = '__all__'


class TimelineSerializer(serializers.ModelSerializer):
    """
    Serializer for Timeline entity
    """

    class Meta:
        model = Timeline
        fields = '__all__'


class PosterSerializer(serializers.ModelSerializer):
    """
    Serializer for Poster entity
    """

    class Meta:
        model = Poster
        fields = '__all__'


class HallSerializer(serializers.ModelSerializer):
    """
    Serializer for Hall entity
    """

    class Meta:
        model = Hall
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    """
    Serializer for Film entity
    """

    def get_code(self):
        """
        Generate ticket's QR code

        :return: unique ticket code
        """
        microsecond = datetime.now().microsecond
        return md5(str(microsecond).encode()).hexdigest()

    def create(self, validated_data):
        """
        Create new Ticket entity using pre-generated unique QR-code

        :param validated_data:
        :return: created Ticket entity
        """

        place = validated_data.get('place')
        status = validated_data.get('status')
        timeline_id = validated_data.get('timeline_id')
        user = validated_data.get('user')
        code = self.get_code()
        ticket = Ticket.objects.create(place=place, status=status, timeline_id=timeline_id, user=user,
                                       code=code)
        return ticket

    class Meta:
        model = Ticket
        fields = '__all__'


UserModel = get_user_model()


class StaffSerializer(serializers.ModelSerializer):
    """
    Serializer for Film entity
    """

    class Meta:
        model = Staff
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for Film entity
    """

    password = serializers.CharField(write_only=True)

    # Тут в ...objects.create(..)  можеш додати ті поля які треба передати
    # і додай їх в Мету
    # і прошу тебе, Андрей, хоть деколи дивись що ти робиш
    # username обезательно бо воно юнік (хз крч)
    def create(self, validated_data):
        """
        Create new User from mobile-client; pay attention on is_staff field - it is False

        :param validated_data:
        :return: created User
        """

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
