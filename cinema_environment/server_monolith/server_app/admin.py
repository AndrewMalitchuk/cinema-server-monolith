from django.contrib import admin

from .models import Film, Cinema, Poster, Timeline, Hall, Ticket


# Register your models here.


class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'duration', 'genre')
    list_display_links = ('title', 'date', 'duration', 'genre')
    search_fields = ('title', 'date', 'genre')


class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'address', 'telephone')
    list_display_links = ('name', 'city', 'address', 'telephone')
    search_fields = ('name', 'city', 'address', 'telephone')


class PosterAdmin(admin.ModelAdmin):
    list_display = ('cinema_id', 'film_id')
    list_display_links = ('cinema_id', 'film_id')
    search_fields = ('cinema_id', 'film_id')


class TimelineAdmin(admin.ModelAdmin):
    list_display = ('cinema_id', 'film_id', 'time', 'date')
    list_display_links = ('cinema_id', 'film_id', 'time', 'date')
    search_fields = ('cinema_id', 'film_id', 'time', 'date')


class HallAdmin(admin.ModelAdmin):
    list_display = ('name', 'cinema_id')
    list_display_links = ('name', 'cinema_id')
    search_fields = ('name', 'cinema_id')


class TicketAdmin(admin.ModelAdmin):
    list_display = ('cinema_id', 'film_id', 'place', 'status', 'user')
    list_display_links = ('cinema_id', 'film_id', 'place', 'status', 'user')
    search_fields = ('cinema_id', 'film_id', 'place', 'status', 'user')


admin.site.register(Film, FilmAdmin)
admin.site.register(Cinema, CinemaAdmin)
admin.site.register(Poster, PosterAdmin)
admin.site.register(Timeline, TimelineAdmin)
admin.site.register(Hall, HallAdmin)
admin.site.register(Ticket, TicketAdmin)
