from django_tables2 import tables, TemplateColumn

from .models import *

from .filters import *


# class CinemaTable(tables.Table):
#     T1 = '<button type="button" class="btn" update-link="{{ record.get_absolute_url_update }}">update</button>'
#     T2 = '<form action="/samples/{{record.id}}/" method="post">{% csrf_token %}<input type="hidden" name="_method" value="delete"><button data-toggle="tooltip" title="Please note that deletion cannot be undone" type="submit" class="btn btn-danger btn-xs">delete</button></form>'
#     T3 = '<button type="button" class="btn btn-info" about-link="{{ record.id }}">About</button>'
#     edit = TemplateColumn(T1)
#     delete = TemplateColumn(T2)
#     about = TemplateColumn(T3)
#
#     class Meta:
#         model = Cinema
#         template_name = "django_tables2/bootstrap.html"
#         fields = ("name", "address", "telephone")


class FilmTable(tables.Table):
    about_col = '<button type="button" class="btn btn-info" about-link="{{ record.id }}">About</button>'
    TemplateColumn(about_col)
    about = TemplateColumn(about_col)



    class Meta:
        model = Film
        template_name = "django_tables2/bootstrap.html"
        fields = ('title', 'date', 'duration', 'genre')




class CinemaTableEditable(tables.Table):
    update_col = '<button type="button" class="btn btn-primary" update-link="{{ record.id }}">Update</button>'
    delete_col = '<button type="button" class="btn btn-danger" delete-link="{{ record.id }}">Delete</button>'
    about_col = '<button type="button" class="btn btn-info" about-link="{{ record.id }}">детальніше</button>'
    TemplateColumn(delete_col, about_col, update_col)
    # TemplateColumn(about_col)
    about = TemplateColumn(about_col)
    delete = TemplateColumn(delete_col)
    update = TemplateColumn(update_col)

    class Meta:
        model = Cinema
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'address', 'city', 'telephone')


class CinemaTableUneditable(tables.Table):
    about_col = '<button type="button" class="btn btn-info" about-link="{{ record.id }}">детальніше</button>'
    TemplateColumn(about_col)
    # TemplateColumn(about_col)
    about = TemplateColumn(about_col)

    class Meta:
        model = Cinema
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'address', 'city', 'telephone')


class PosterTable(tables.Table):
    delete_col = '<button type="button" class="btn btn-danger" delete-link="{{ record.id }}">Delete</button>'
    TemplateColumn(delete_col)
    delete = TemplateColumn(delete_col)

    class Meta:
        model = Poster
        template_name = "django_tables2/bootstrap.html"
        fields = ('film_id', 'cinema_id')


class TicketTable(tables.Table):
    class Meta:
        model = Ticket
        template_name = "django_tables2/bootstrap.html"
        fields = ('cinema_id', 'film_id', 'place', 'date', 'status')


class HallTable(tables.Table):
    update_col = '<button type="button" class="btn btn-primary" update-link="{{ record.id }}" cinema-id="{{record.cinema_id.id}}">Update</button>'
    delete_col = '<button type="button" class="btn btn-danger" delete-link="{{ record.id }}">Delete</button>'
    TemplateColumn(delete_col, update_col)
    delete = TemplateColumn(delete_col)
    update = TemplateColumn(update_col)

    class Meta:
        model = Hall
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'cinema_id')


class TimelineTable(tables.Table):
    delete_col = '<button type="button" class="btn btn-danger" delete-link="{{ record.id }}">Delete</button>'
    TemplateColumn(delete_col)
    delete = TemplateColumn(delete_col)

    class Meta:
        model = Timeline
        template_name = "django_tables2/bootstrap.html"
        fields = ('film_id', 'cinema_id', 'date','time')
