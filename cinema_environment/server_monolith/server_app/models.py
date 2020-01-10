from django.db import models
from django.conf import settings


class Film(models.Model):
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
        error_messages="Помилка введеного значення",
        help_text="Назва фільму (до 256 символів)",
        unique=True
    )

    description = models.TextField(
        verbose_name="Опис",
        max_length=512,
        error_messages="Помилка введеного значення",
        help_text="Опис фільму (до 512 символів)"
    )

    date = models.DateField(
        verbose_name="Дата",
        auto_now_add=True,
        error_messages="Помилка введеного значення",
        help_text="Дата прем'єри")

    duration = models.IntegerField(
        verbose_name="Тривалість",
        error_messages="Помилка введеного значення",
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

    pic_url = models.ImageField()

    def __str__(self):
        return self.title


class Cinema(models.Model):
    app_label = "server_app.apps.ServerAppConfig"

    class Meta:
        verbose_name_plural = "Кінотеатри"
        verbose_name = "Кінотеатр"
        ordering = ['-city']

    name = models.CharField(
        verbose_name="Назва",
        max_length=256,
        error_messages="Помилка введеного значення",
        help_text="Назва кінотеатру (до 256 символів)"
    )

    address = models.TextField(
        verbose_name="Адреса",
        max_length=256,
        error_messages="Помилка введеного значення",
        help_text="Адреса кінотеатру (до 256 символів)"
    )

    city = models.CharField(
        verbose_name="Місто",
        max_length=128,
        error_messages="Помилка введеного значення",
        help_text="Назва міста (до 128 символів)"
    )

    telephone = models.CharField(
        verbose_name="Телефон",
        max_length=20,
        error_messages="Помилка введеного значення",
        help_text="Telephone regexp !!!"
    )

    geo_lat = models.FloatField(
        verbose_name="Координати: широта"
    )

    geo_lon = models.FloatField(
        verbose_name="Координати: довгота"
    )

    pic_url = models.ImageField()

    def __str__(self):
        return self.name + " [" + self.city + "]"


class Poster(models.Model):
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


class Timeline(models.Model):
    app_label = "server_app.apps.ServerAppConfig"

    class Meta:
        verbose_name = "Розклад"
        verbose_name_plural = "Розклад"
        ordering = ['-date']

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

    time = models.TimeField(
        verbose_name="Час"
    )

    date = models.DateField(
        verbose_name="Дата"
    )


class Hall(models.Model):
    app_label = "server_app.apps.ServerAppConfig"

    class Meta:
        verbose_name = "Зал"
        verbose_name_plural = "Зали"
        ordering = ['-name']

    name = models.CharField(
        verbose_name="Назва залу",
        max_length=128,
        help_text="Назва залу"
    )

    cinema_id = models.ForeignKey(
        Cinema,
        on_delete=models.DO_NOTHING,
        verbose_name="Cinema ID"
    )

    # TODO: change to JSONField
    hall_json = models.TextField(verbose_name="JSON")


class Ticket(models.Model):
    app_label = "server_app.apps.ServerAppConfig"

    class Meta:
        verbose_name = "Білети"
        verbose_name_plural = "Білет"

    STATUS = (
        (1, 'Returned'),
        (2, 'Active'),
        (3, 'Canceled')
    )

    cinema_id = models.ForeignKey(
        Cinema,
        on_delete=models.DO_NOTHING,
        verbose_name="Cinema"
    )

    film_id = models.ForeignKey(
        Film,
        on_delete=models.DO_NOTHING,
        verbose_name="Film ID"
    )

    place = models.CharField(
        verbose_name="Місце",
        max_length=32,
        error_messages="Помилка введеного значення",
        help_text="Місце в залі"
    )

    code = models.CharField(
        verbose_name="Код",
        max_length=1024
    )

    status = models.PositiveIntegerField(
        choices=STATUS,
        default=2,
        verbose_name="Статус"
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
