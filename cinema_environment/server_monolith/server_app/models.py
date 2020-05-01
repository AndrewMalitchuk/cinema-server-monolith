from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
import datetime


class Film(models.Model):
    """
    A class that represents Film entity

    Attributes:
        GENRE (enum): An enumeration for available genres
        title (str): A film's title
        description (str): A film's description
        date: A film's date
        duration: A film's duration
        genre: A film's genre
        video_url: A film's trailer URL (youtube)
        pic_url: A film's poster URL
    """

    app_label = "server_app.apps.ServerAppConfig"

    class Meta:
        verbose_name_plural = "Фільми"
        verbose_name = "Фільм"
        ordering = ['-title']

    GENRE = (
        (1, 'Comedy'),
        (2, 'Action'),
        (3, 'Historical'),
        (4, 'Sci-Fi'),
        (5, 'Horror'),
    )

    title = models.CharField(
        verbose_name="Назва",
        max_length=256,
        help_text="Назва фільму"

    )

    description = models.TextField(
        verbose_name="Опис",
        max_length=512,
        help_text="Опис фільму"
    )

    date = models.DateField(
        verbose_name="Дата",
        auto_now_add=True,
        help_text="Дата прем'єри"
    )

    duration = models.IntegerField(
        verbose_name="Тривалість",
        help_text="Тривалість фільму"
    )

    genre = models.PositiveIntegerField(
        verbose_name="Жанр",
        help_text="Жанр фільму",
        choices=GENRE,
        default=2
    )

    video_url = models.URLField(
        verbose_name="Трейлер",
        help_text="Посилання на YouTube",
    )

    pic_url = models.ImageField(upload_to="film/poster/", verbose_name="Постер фільму")

    def __str__(self):
        return self.title


class Cinema(models.Model):
    """
    A class that represents Cinema entity

    Attributes:
        name: A cinema's name
        address: A cinema's address in current city
        city: City's name
        telephone: A cinema's telephone
        geo_lat: Latitude for location on the map
        geo_lon: Longitude for location on the map
        pic_url: A cinema's picture/logo URL
    """

    app_label = "server_app.apps.ServerAppConfig"

    class Meta:
        verbose_name_plural = "Кінотеатри"
        verbose_name = "Кінотеатр"
        ordering = ['-city']

    name = models.CharField(
        verbose_name="Назва",
        max_length=256,
        help_text="Назва кінотеатру"
    )

    address = models.TextField(
        verbose_name="Адреса",
        max_length=256,
        help_text="Адреса кінотеатру"
    )

    city = models.CharField(
        verbose_name="Місто",
        max_length=128,
    )

    telephone = models.CharField(
        verbose_name="Телефон",
        max_length=20,
        help_text="Контактний телефон"
    )

    geo_lat = models.FloatField(
        verbose_name="Координати: широта"
    )

    geo_lon = models.FloatField(
        verbose_name="Координати: довгота"
    )

    pic_url = models.ImageField(upload_to="cinema/pic/", verbose_name="Зображення кінотеатру")

    def __str__(self):
        return self.name


class Poster(models.Model):
    """
    A class that represents Poster entity

    Attributes:
        cinema_id: Cinema's ID for linking
        film_id: Film's ID for linking
    """

    app_label = "server_app.apps.ServerAppConfig"

    class Meta:
        verbose_name_plural = "Афіши"
        verbose_name = "Афіша"

    cinema_id = models.ForeignKey(
        Cinema,
        on_delete=models.DO_NOTHING,
        verbose_name="Cinema ID"
    )
    film_id = models.ForeignKey(
        Film,
        on_delete=models.DO_NOTHING,
        verbose_name="Film ID"
    )


class Hall(models.Model):
    """
    A class that represents Hall entity

    Attributes:
        name: A hall's name
        cinema_id: Cinema's ID for linking
        hall_json: JSON-entity for hall rendering
    """

    app_label = "server_app.apps.ServerAppConfig"

    class Meta:
        verbose_name = "Зал"
        verbose_name_plural = "Зали"
        ordering = ['-name']

    name = models.CharField(
        verbose_name="Назва залу",
        max_length=128,
        help_text="Найменування залу"
    )

    cinema_id = models.ForeignKey(
        Cinema,
        on_delete=models.DO_NOTHING,
        verbose_name="Cinema ID"
    )

    hall_json = models.TextField(verbose_name="JSON")

    def __str__(self):
        return self.name


class Timeline(models.Model):
    """
    A class that represents Timeline entity

    Attributes:
        cinema_id: Cinema's ID for linking
        film_id: Film's ID for linking
        hall_id: Hall's ID for linking
        time: A session's time
        date: A session's date
        price: A price for current price
    """

    app_label = "server_app.apps.ServerAppConfig"

    class Meta:
        verbose_name = "Розклад"
        verbose_name_plural = "Розклад"

    cinema_id = models.ForeignKey(
        Cinema,
        on_delete=models.DO_NOTHING,
        verbose_name="Cinema ID"
    )

    film_id = models.ForeignKey(
        Film,
        on_delete=models.DO_NOTHING,
        verbose_name="Film ID"
    )

    hall_id = models.ForeignKey(
        Hall,
        on_delete=models.DO_NOTHING,
        verbose_name="Hall ID"
    )

    time = models.TimeField(
        verbose_name="Час",
        help_text="Час показу",
        default=datetime.time(00, 00))

    date = models.DateField(
        verbose_name="Дата",
        help_text="Дата показу",
        default=datetime.date.today
    )

    price = models.DecimalField(
        verbose_name="Ціна",
        max_digits=5,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return self.film_id.title + " | " + self.cinema_id.name


class Ticket(models.Model):
    """
    A class that represents Ticket entity

    Attributes:
        STATUS: A enumeration that contains Ticket's status
        place: Place in hall for current session
        status: Ticket's status
        user: A User's ID
        timeline_id: Timeline's ID for linking
    """

    app_label = "server_app.apps.ServerAppConfig"

    class Meta:
        verbose_name = "Білети"
        verbose_name_plural = "Білет"

    STATUS = (
        (1, 'Returned'),
        (2, 'Active'),
        (3, 'Canceled')
    )

    place = models.CharField(
        verbose_name="Місце",
        max_length=32,
        help_text="Місце у залі"
    )

    code = models.CharField(
        verbose_name="Код",
        max_length=1024,
        null=True,
        blank=True
    )

    status = models.PositiveIntegerField(
        choices=STATUS,
        default=2,
        verbose_name="Статус",
        help_text="Статус квитка"
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    timeline_id = models.ForeignKey(
        Timeline,
        on_delete=models.CASCADE,
        verbose_name="Сеанс"
    )


class Staff(models.Model):
    """
    A class that represents Staff entity.

    Attributes:
        user_id: User's ID for linking
        cinema_id: Cinema's ID for linking
    """

    app_label = "server_app.apps.ServerAppConfig"

    class Meta:
        verbose_name_plural = "Персонал"
        verbose_name = "Персонал"

    user_id = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name="User ID"
    )

    cinema_id = models.ForeignKey(
        Cinema,
        on_delete=models.DO_NOTHING,
        verbose_name="Cinema ID"
    )
