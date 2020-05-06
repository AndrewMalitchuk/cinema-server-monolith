from django_tables2 import tables, TemplateColumn

from .models import *


class FilmTable(tables.Table):
    """
    Table for Film entities; used for generation bootstrap-table

    Attributes:
        about_col: extra column for opening "About Film" page
    """

    about_col = '<button type="button" class="btn btn-info" about-link="{{ record.id }}">About</button>'
    TemplateColumn(about_col)
    about = TemplateColumn(about_col)

    class Meta:
        model = Film
        template_name = "django_tables2/bootstrap.html"
        fields = ('title', 'date', 'duration', 'genre')


class CinemaTableEditable(tables.Table):
    """
    Table for Cinema entities (editable); used for generation bootstrap-table

    Attributes:
        update_col: extra column for updating entity
        delete_col: extra column for deleting entity
        about_col: extra column for opening "About Cinema" page
    """

    # For this time, update and about is enough
    update_col = '<button type="button" class="btn btn-primary" update-link="{{ record.id }}">Update</button>'
    # delete_col = '<button type="button" class="btn btn-danger" delete-link="{{ record.id }}">Delete</button>'
    about_col = '<button type="button" class="btn btn-info" about-link="{{ record.id }}">детальніше</button>'
    # TemplateColumn(delete_col, about_col, update_col)
    TemplateColumn(about_col, update_col)
    about = TemplateColumn(about_col)
    # delete = TemplateColumn(delete_col)
    update = TemplateColumn(update_col)

    class Meta:
        model = Cinema
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'address', 'telephone')


class CinemaTableUneditable(tables.Table):
    """
    Table for Cinema entities (uneditable); used for generation bootstrap-table

    Attributes:
        about_col: extra column for opening "About Cinema" page
    """

    about_col = '<button type="button" class="btn btn-info" about-link="{{ record.id }}">детальніше</button>'
    TemplateColumn(about_col)
    about = TemplateColumn(about_col)

    class Meta:
        model = Cinema
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'address', 'telephone')


class PosterTable(tables.Table):
    """
    Table for Poster entities; used for generation bootstrap-table

    Attributes:
        delete_col: extra column for deleting entity
    """

    delete_col = '<button type="button" class="btn btn-danger" delete-link="{{ record.id }}">Delete</button>'
    TemplateColumn(delete_col)
    delete = TemplateColumn(delete_col)

    class Meta:
        model = Poster
        template_name = "django_tables2/bootstrap.html"
        fields = ('film_id', 'cinema_id')


class TicketTable(tables.Table):
    """
    Table for Ticket entities; used for generation bootstrap-table
    """

    class Meta:
        model = Ticket
        template_name = "django_tables2/bootstrap.html"
        fields = ('cinema_id', 'film_id', 'place', 'date', 'status')


class HallTable(tables.Table):
    """
    Table for Hall entities; used for generation bootstrap-table

    Attributes:
        update_col: extra column for updating entity
        delete_col: extra column for deleting entity
    """

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
    """
    Table for Timeline entities; used for generation bootstrap-table

    Attributes:
        delete_col: extra column for deleting entity
    """

    delete_col = '<button type="button" class="btn btn-danger" delete-link="{{ record.id }}">Delete</button>'
    TemplateColumn(delete_col)
    delete = TemplateColumn(delete_col)

    class Meta:
        model = Timeline
        template_name = "django_tables2/bootstrap.html"
        fields = ('film_id', 'cinema_id', 'date', 'time')
