from django.urls import path

from .views import *

app_name = 'film'

urlpatterns = [

    # REST API
    path('film/', api_film),
    path('cinema/', api_cinema),
    path('timeline/', api_timeline),
    path('poster/', api_poster),
    path('hall/', api_hall),
    path('ticket/', api_ticket),
    path('user/', api_user),
    path('create/', CreateUserView.as_view()),
    path('staff/',get_staff_job),

    # Film Web
    path('film/all', FilmTableView.as_view()),
    path('film/<int:film_id>', about_film),

    # Cinema Web
    path('cinema/all', cinema_table_all),
    path('form/cinema/<int:cinema_id>/update', form_cinema_update),
    path('form/cinema/insert', form_cinema_insert),
    path('cinema/<int:cinema_id>', cinema_profile),

    # Poster Web
    path('table/poster/<int:cinema_id>', get_poster_table_by_cinema_id),
    path('form/poster/<int:cinema_id>/insert', form_poster_insert),

    # Timeline Web
    path('table/timeline/<int:cinema_id>', get_timeline_table_by_cinema_id),
    path('form/timeline/<int:cinema_id>/insert', form_timeline_insert),

    # Hall Web
    path('table/hall/<int:cinema_id>', get_hall_table_by_cinema_id),
    path('form/hall/<int:cinema_id>/insert', form_hall_insert),
    path('form/hall/<int:cinema_id>/<int:hall_id>/update', form_hall_update),

    # Info pages
    path('about_dev/',about_dev),
    path('about_project/',about_project),

]
