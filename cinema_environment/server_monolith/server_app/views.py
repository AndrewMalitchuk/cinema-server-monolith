import os

from django.shortcuts import render
from rest_framework import generics, views, settings
from django.http import JsonResponse, Http404, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Film
from .serializers import FilmSerializer


@api_view(['GET'])
def api_films(request):
    if request.method == 'GET':
        films = Film.objects.all()
        title = request.GET.get('title', None)
        date = request.GET.get('date', None)
        id = request.GET.get('id', None)
        serializer = FilmSerializer(films, many=True)

        if title is not None:
            films = Film.objects.get(title=title)
            serializer = FilmSerializer(films)
        elif date is not None:
            films = Film.objects.filter(date=date)
            serializer = FilmSerializer(films, many=True)
        elif id is not None:
            films = Film.objects.get(pk=id)
            serializer = FilmSerializer(films)

        return Response(serializer.data)
