from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Film, Cinema, Timeline, Poster, Hall, Ticket
from .serializers import FilmSerializer, CinemaSerializer, TimelineSerializer, PosterSerializer, HallSerializer, \
    TicketSerializer, RegistrationSerializer


@api_view(['GET'])
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

        return Response(serializer.data)


@api_view(['GET'])
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

        return Response(serializer.data)


@api_view(['GET'])
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

        return Response(serializer.data)


@api_view(['GET'])
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

        return Response(serializer.data)


@api_view(['GET'])
def api_hall(request):
    if request.method == 'GET':
        hall = Hall.objects.all()
        serializer = HallSerializer(hall, many=True)

        cinema_id = request.GET.get('cinema_id', None)

        if cinema_id is not None:
            hall = Hall.objects.get(cinema_id=cinema_id)
            serializer = HallSerializer(hall)

        return Response(serializer.data)


@api_view(['GET'])
def api_ticket(request):
    if request.method == 'GET':
        ticket = Ticket.objects.all()
        serializer = TicketSerializer(ticket, many=True)

        film_id = request.GET.get('film_id', None)
        user_id = request.GET.get('user_id', None)

        if film_id is not None and user_id is not None:
            ticket = Ticket.objects.filter(film_id=film_id, user=user_id)
            serializer = TicketSerializer(ticket, many=True)
        elif user_id is not None:
            ticket = Ticket.objects.filter(user=user_id)
            serializer = TicketSerializer(ticket, many=True)

        return Response(serializer.data)


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


@api_view(['POST'])
def api_registration(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.create()
            data={}
            data['username']=account.username
            return Response(data)
