from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import *

app_name = 'film'
urlpatterns = [
    path('films/', api_films),


]
