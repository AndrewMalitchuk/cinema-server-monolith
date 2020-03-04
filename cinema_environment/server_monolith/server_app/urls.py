from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

app_name = 'film'
urlpatterns = [
    path('film/', api_film),
    path('cinema/', api_cinema),
    path('timeline/', api_timeline),
    path('poster/', api_poster),
    path('hall/', api_hall),
    path('ticket/', api_ticket),
    path('user/', api_user),
    path('create/', CreateUserView.as_view()),
    path('hall_form/', hall_form),
    path('form/cinema/<int:cinema_id>/update', form_cinema_udpate),
    path('form/cinema/insert', form_cinema_insert),
    path('email/', email),
    path("forms/cinema", mypage),
    path('export/', table_view),
    path('table/cinema', CinemaTableView.as_view()),
    path('table/film', FilmTableView.as_view()),
    path('table/poster/<int:cinema_id>', get_poster_table_by_cinema_id),
    path('table/ticket/<int:cinema_id>', get_ticket_table_by_cinema_id),
    path('table/ticket/<int:cinema_id>/<int:film_id>', get_ticket_table_by_cinema_id_and_film_id),
    path('table/hall/<int:cinema_id>', get_hall_table_by_cinema_id),
    path('table/timeline/<int:cinema_id>', get_timeline_table_by_cinema_id),

]

# handler404 = handler404
