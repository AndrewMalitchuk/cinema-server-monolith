from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializers import *


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def api_film(request):
    if request.method == 'GET':
        films = Film.objects.all()
        serializer = FilmSerializer(films, many=True)

        title = request.GET.get('title', None)
        date = request.GET.get('date', None)
        id = request.GET.get('id', None)
        genre = request.GET.get('genre', None)

        if title is not None:
            films = Film.objects.get(title=title)
            serializer = FilmSerializer(films)
        elif date is not None:
            films = Film.objects.filter(date=date)
            serializer = FilmSerializer(films, many=True)
        elif id is not None:
            films = Film.objects.get(pk=id)
            serializer = FilmSerializer(films)
        elif genre is not None:
            films = Film.objects.get(genre=genre)
            serializer = FilmSerializer(films, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        id = request.GET.get('id', None)

        if id is not None:
            film = Film.objects.get(pk=id)
            serializer = FilmSerializer(film, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK)
            else:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        id = request.GET.get('id', None)

        if id is not None:
            film = Film.objects.get(pk=id)
            film.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def api_cinema(request):
    if request.method == 'GET':
        cinemas = Cinema.objects.all()
        serializer = CinemaSerializer(cinemas, many=True)

        id = request.GET.get('id', None)
        name = request.GET.get('name', None)
        city = request.GET.get('city', None)

        if id is not None:
            cinemas = Cinema.objects.get(pk=id)
            serializer = CinemaSerializer(cinemas)
        elif name is not None:
            cinemas = Cinema.objects.filter(name=name)
            serializer = CinemaSerializer(cinemas, many=True)
        elif city is not None:
            cinemas = Cinema.objects.filter(city=city)
            serializer = CinemaSerializer(cinemas, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CinemaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        id = request.GET.get('id', None)

        if id is not None:
            cinema = Cinema.objects.get(pk=id)
            serializer = CinemaSerializer(cinema, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK)
            else:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        id = request.GET.get('id', None)

        if id is not None:
            cinema = Cinema.objects.get(pk=id)
            cinema.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def api_timeline(request):
    if request.method == 'GET':
        timeline = Timeline.objects.all()
        serializer = TimelineSerializer(timeline, many=True)

        cinema_id = request.GET.get('cinema_id', None)
        film_id = request.GET.get('film_id', None)
        date = request.GET.get('date', None)

        if cinema_id is not None and film_id is not None:
            timeline = Timeline.objects.filter(cinema_id=cinema_id, film_id=film_id)
            serializer = TimelineSerializer(timeline, many=True)
        elif cinema_id is not None:
            timeline = Timeline.objects.filter(cinema_id=cinema_id)
            serializer = TimelineSerializer(timeline, many=True)
        elif film_id is not None:
            timeline = Timeline.objects.filter(film_id=film_id)
            serializer = TimelineSerializer(timeline, many=True)
        elif date is not None:
            timeline = Timeline.objects.filter(date=date)
            serializer = TimelineSerializer(timeline, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TimelineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        id = request.GET.get('id', None)

        if id is not None:
            timeline = Timeline.objects.get(pk=id)
            serializer = TimelineSerializer(timeline, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        id = request.GET.get('id', None)

        if id is not None:
            timeline = Timeline.objects.get(pk=id)
            timeline.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def api_poster(request):
    if request.method == 'GET':

        poster = Poster.objects.all()
        serializer = PosterSerializer(poster, many=True)

        cinema_id = request.GET.get('cinema_id', None)
        film_id = request.GET.get('film_id', None)

        if cinema_id is not None and film_id is not None:
            poster = Poster.objects.filter(cinema_id=cinema_id, film_id=film_id)
            serializer = PosterSerializer(poster, many=True)
        elif cinema_id is not None:
            poster = Poster.objects.filter(cinema_id=cinema_id)
            serializer = PosterSerializer(poster, many=True)
        elif film_id is not None:
            poster = Poster.objects.filter(film_id=film_id)
            serializer = PosterSerializer(poster, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = PosterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        id = request.GET.get('id', None)

        if id is not None:
            poster = Poster.objects.get(pk=id)
            serializer = PosterSerializer(poster, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK)
            else:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        id = request.GET.get('id', None)

        if id is not None:
            poster = Poster.objects.get(pk=id)
            poster.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def api_hall(request):
    if request.method == 'GET':
        hall = Hall.objects.all()
        serializer = HallSerializer(hall, many=True)

        cinema_id = request.GET.get('cinema_id', None)
        id = request.GET.get('id', None)

        if cinema_id is not None:
            hall = Hall.objects.get(cinema_id=cinema_id)
            serializer = HallSerializer(hall)
        elif id is not None:
            hall = Hall.objects.get(pk=id)
            serializer = HallSerializer(hall)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = HallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        id = request.GET.get('id', None)

        if id is not None:
            hall = Hall.objects.get(pk=id)
            serializer = HallSerializer(hall, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK)
            else:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        id = request.GET.get('id', None)

        if id is not None:
            hall = Hall.objects.get(pk=id)
            hall.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def api_ticket(request):
    if request.method == 'GET':
        ticket = Ticket.objects.all()
        serializer = TicketSerializer(ticket, many=True)

        film_id = request.GET.get('film_id', None)
        user_id = request.GET.get('user_id', None)
        code = request.GET.get('code', None)

        if film_id is not None and user_id is not None:
            ticket = Ticket.objects.filter(film_id=film_id, user=user_id)
            serializer = TicketSerializer(ticket, many=True)
        elif user_id is not None:
            ticket = Ticket.objects.filter(user=user_id)
            serializer = TicketSerializer(ticket, many=True)
        elif code is not None:
            ticket = Ticket.objects.get(code=code)
            serializer = TicketSerializer(ticket)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        id = request.GET.get('id', None)

        if id is not None:
            ticket = Ticket.objects.get(pk=id)
            serializer = TicketSerializer(ticket, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK)
            else:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        id = request.GET.get('id', None)

        if id is not None:
            ticket = Ticket.objects.get(pk=id)
            ticket.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api_user(request):
    if request.method == 'GET':
        user = request.user
        return Response({
            'id': user.pk,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_staff': user.is_staff,
            'is_active': user.is_active
        })


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer
