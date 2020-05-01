from django.contrib import admin

from .models import Film, Cinema, Poster, Timeline, Hall, Ticket, Staff


class FilmAdmin(admin.ModelAdmin):
    """
        A class for displaying Film entity in proper way for Admin-page

        Attributes:
            list_display: A list of fields for displaying in Admin-page
            list_display_links: A list of fields for links
            search_fields: A list of fields for searching
    """
    list_display = ('title', 'date', 'duration', 'genre')
    list_display_links = ('title', 'date', 'duration', 'genre')
    search_fields = ('title', 'date', 'genre')


class CinemaAdmin(admin.ModelAdmin):
    """
        A class for displaying Cinema entity in proper way for Admin-page

        Attributes:
            list_display: A list of fields for displaying in Admin-page
            list_display_links: A list of fields for links
            search_fields: A list of fields for searching
    """
    list_display = ('name', 'city', 'address', 'telephone')
    list_display_links = ('name', 'city', 'address', 'telephone')
    search_fields = ('name', 'city', 'address', 'telephone')


class PosterAdmin(admin.ModelAdmin):
    """
        A class for displaying Poster entity in proper way for Admin-page

        Attributes:
            list_display: A list of fields for displaying in Admin-page
            list_display_links: A list of fields for links
            search_fields: A list of fields for searching
    """
    list_display = ('cinema_id', 'film_id')
    list_display_links = ('cinema_id', 'film_id')
    search_fields = ('cinema_id', 'film_id')


class TimelineAdmin(admin.ModelAdmin):
    """
        A class for displaying Timeline entity in proper way for Admin-page

        Attributes:
            list_display: A list of fields for displaying in Admin-page
            list_display_links: A list of fields for links
            search_fields: A list of fields for searching
    """
    list_display = ('cinema_id', 'film_id', 'hall_id', 'date', 'time', 'price')
    list_display_links = ('cinema_id', 'film_id', 'hall_id', 'date', 'time', 'price')
    search_fields = ('cinema_id', 'film_id', 'hall_id', 'date', 'time', 'price')


class HallAdmin(admin.ModelAdmin):
    """
        A class for displaying Hall entity in proper way for Admin-page

        Attributes:
            list_display: A list of fields for displaying in Admin-page
            list_display_links: A list of fields for links
            search_fields: A list of fields for searching
    """
    list_display = ('name', 'cinema_id')
    list_display_links = ('name', 'cinema_id')
    search_fields = ('name', 'cinema_id')


class TicketAdmin(admin.ModelAdmin):
    """
        A class for displaying Ticket entity in proper way for Admin-page

        Attributes:
            list_display: A list of fields for displaying in Admin-page
            list_display_links: A list of fields for links
            search_fields: A list of fields for searching
    """
    list_display = ('place', 'status', 'user')
    list_display_links = ('place', 'status', 'user')
    search_fields = ('place', 'status', 'user')


class StaffAdmin(admin.ModelAdmin):
    """
        A class for displaying Staff entity in proper way for Admin-page

        Attributes:
            list_display: A list of fields for displaying in Admin-page
            list_display_links: A list of fields for links
            search_fields: A list of fields for searching
    """
    list_display = ('cinema_id', 'user_id')
    list_display_links = ('cinema_id', 'user_id')
    search_fields = ('cinema_id', 'user_id')


# Adding custom Admin-pages for entities
admin.site.register(Film, FilmAdmin)
admin.site.register(Cinema, CinemaAdmin)
admin.site.register(Poster, PosterAdmin)
admin.site.register(Timeline, TimelineAdmin)
admin.site.register(Hall, HallAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Staff, StaffAdmin)
