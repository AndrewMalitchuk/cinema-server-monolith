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
    path('cinema_form/', cinema_form),
    path('email/', email),

]
