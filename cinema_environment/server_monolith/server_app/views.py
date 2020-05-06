from django.shortcuts import render
from django_tables2 import SingleTableView, RequestConfig
from django_tables2.export import ExportMixin
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .forms import *
from .permission import IsStaffOrAdminWriteOnly
from .serializers import *
from .tables import *


# REST API

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsStaffOrAdminWriteOnly])
def api_film(request):
    """
    REST endpoint for Film entity

    :param request:
    :return: Film entity
    """

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
            films = Film.objects.filter(genre=genre)
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
@permission_classes([IsStaffOrAdminWriteOnly])
def api_cinema(request):
    """
    REST endpoint for Cinema entity

    :param request:
    :return: Cinema entity
    """

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
            cinemas = Cinema.objects.get(name=name)
            serializer = CinemaSerializer(cinemas, many=False)
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
@permission_classes([IsStaffOrAdminWriteOnly])
def api_timeline(request):
    """
    REST endpoint for Timeline entity

    :param request:
    :return: Cinema entity
    """

    if request.method == 'GET':
        timeline = Timeline.objects.all()
        serializer = TimelineSerializer(timeline, many=True)
        cinema_id = request.GET.get('cinema_id', None)
        film_id = request.GET.get('film_id', None)
        id = request.GET.get('id', None)
        date = request.GET.get('date', None)
        if cinema_id is not None and film_id is not None and date is None:
            timeline = Timeline.objects.filter(cinema_id=cinema_id, film_id=film_id)
            serializer = TimelineSerializer(timeline, many=True)
        elif cinema_id is not None and film_id is None and date is not None:
            timeline = Timeline.objects.filter(cinema_id=cinema_id, date=date)
            serializer = TimelineSerializer(timeline, many=True)
        elif cinema_id is not None and film_id is not None and date is not None:
            timeline = Timeline.objects.filter(cinema_id=cinema_id, film_id=film_id, date=date)
            serializer = TimelineSerializer(timeline, many=True)
        elif cinema_id is not None and film_id is None and date is None:
            timeline = Timeline.objects.filter(cinema_id=cinema_id)
            serializer = TimelineSerializer(timeline, many=True)
        elif cinema_id is None and film_id is not None and date is None:
            timeline = Timeline.objects.filter(film_id=film_id)
            serializer = TimelineSerializer(timeline, many=True)
        elif cinema_id is None and film_id is None and date is not None:
            timeline = Timeline.objects.filter(date=date)
            serializer = TimelineSerializer(timeline, many=True)
        elif id is not None:
            timeline = Timeline.objects.get(id=id)
            serializer = TimelineSerializer(timeline)
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
@permission_classes([IsStaffOrAdminWriteOnly])
def api_poster(request):
    """
    REST endpoint for Poster entity

    :param request:
    :return: Poster entity
    """

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
@permission_classes([AllowAny])
def api_hall(request):
    """
    REST endpoint for Hall entity

    :param request:
    :return: Hall entity
    """

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
@permission_classes([IsAuthenticated])
def api_ticket(request):
    """
    REST endpoint for Ticket entity

    :param request:
    :return: Ticket entity
    """

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
@permission_classes([IsStaffOrAdminWriteOnly])
def get_staff_job(request):
    """
    REST endpoint for Staff entity; used for getting Staff' job

    :param request:
    :return: Staff entity
    """

    if request.method == 'GET':
        user_id = request.GET.get('user_id', None)
        if user_id is not None:
            staff = Staff.objects.get(user_id=user_id)
            cinema = Cinema.objects.get(pk=staff.cinema_id.id)
            serializer = CinemaSerializer(cinema, many=False)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_user(request):
    """
    REST endpoint for User entity

    :param request:
    :return: User entity
    """

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
    """
    REST endpoint for creating new user
    """

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


# Web

# @permission_classes([AllowAny])
# def hall_form(request):
#     """
#
#     :param request:
#     :return:
#     """
#     if request.method == "POST":
#         form = HallForm(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=True)
#             instance.save()
#     else:
#         form = HallForm()
#     return render(request, "forms/hall_form.html", {"form": form})


@permission_classes([AllowAny])
def cinema_profile(request, cinema_id):
    """
    Get Cinema's profile

    :param request:
    :param cinema_id: current cinema's ID
    :return: chosen Cinema
    """

    form = Cinema.objects.get(pk=cinema_id)
    if request.user.pk is not None:
        return render(request, "pages/cinema-profile.html",
                      {"form": form, "staff": Staff.objects.get(user_id=request.user.pk)})
    else:
        return render(request, "pages/cinema-profile.html",
                      {"form": form})


@permission_classes([AllowAny])
def about_film(request, film_id):
    """
    Get Film's info

    :param request:
    :param film_id: current Film's ID
    :return: chosen Film
    """

    form = Film.objects.get(pk=film_id)
    if request.user.pk is not None:
        return render(request, "pages/about-film.html",
                      {"form": form, "staff": Staff.objects.get(user_id=request.user.pk)})
    else:
        return render(request, "pages/about-film.html", {"form": form})


@permission_classes([AllowAny])
def about_dev(request):
    """
    Get about dev page

    :param request:
    :return: about dev page
    """
    if request.user.pk is not None:
        return render(request, "pages/about-dev.html",
                      {"staff": Staff.objects.get(user_id=request.user.pk)})
    else:
        return render(request, 'pages/about-dev.html')


@permission_classes([AllowAny])
def about_project(request):
    """
    Get about project page

    :param request:
    :return: about project page
    """

    if request.user.pk is not None:
        return render(request, "pages/about-project.html",
                      {"staff": Staff.objects.get(user_id=request.user.pk)})
    else:
        return render(request, 'pages/about-project.html')


class FilmTableView(ExportMixin, SingleTableView):
    """
    Get all Films entities as a table
    """

    model = Film
    table_class = FilmTable
    template_name = 'tables/film-table.html'

    def get(self, request, *args, **kwargs):
        """
        Returns Film's table

        :param request:
        :param args:
        :param kwargs:
        :return: Film's table
        """
        if request.user.pk is not None:
            return render(request, "tables/film-table.html",
                          {'table': FilmTable(Film.objects.all()), 'staff': Staff.objects.get(user_id=request.user.pk)})
        else:
            return render(request, "tables/film-table.html", {'table': FilmTable(Film.objects.all())})


def cinema_table_all(request):
    """
    Returns all Cinema entities as a table

    :param request:
    :return: Cinema's table
    """

    config = RequestConfig(request)
    if request.user.is_staff is True:
        content = CinemaTableEditable(Cinema.objects.all())
        config.configure(content)
        return render(request, 'tables/cinema/cinema-table-editable.html', {
            'table': content,
            'cinema_id': Staff.objects.get(user_id=request.user.pk).cinema_id.id,
            "staff": Staff.objects.get(user_id=request.user.pk)
        })
    else:
        content = CinemaTableUneditable(Cinema.objects.all())
        config.configure(content)
        return render(request, 'tables/cinema/cinema-table-uneditable.html', {
            'table': content,
        })


@permission_classes([AllowAny])
def form_cinema_update(request, cinema_id):
    """
    Returns Cinema's update form

    :param request:
    :param cinema_id: Cinema's ID for updating
    :return: web-page for updating
    """

    if request.user.is_staff is True:
        if Staff.objects.get(user_id=request.user.pk).cinema_id.id == cinema_id:
            if request.method == "POST":
                form = CinemaForm(request.POST, request.FILES)
                if form.is_valid():
                    instance = form.save(commit=True)
                    instance.save()
            else:
                form = Cinema.objects.get(pk=cinema_id)
            return render(request, "forms/cinema/cinema-update.html",
                          {"form": form, "staff": Staff.objects.get(user_id=request.user.pk)})
        else:
            return render(request, "404.html", {})
    else:
        return render(request, "404.html", {})


@permission_classes([AllowAny])
def form_cinema_insert(request):
    """
    Returns Cinema's insert form

    :param request:
    :return: web-page for creating new entity
    """

    if request.user.is_staff is True:
        if request.method == "POST":
            form = CinemaForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=True)
                instance.save()
        else:
            form = CinemaForm()
        return render(request, "forms/cinema/cinema-insert.html",
                      {"form": form, "staff": Staff.objects.get(user_id=request.user.pk)})
    else:
        return render(request, "404.html", {})


def get_poster_table_by_cinema_id(request, cinema_id):
    """
    Returns all Poster entities with certain Cinema's ID value

    :param request:
    :param cinema_id: linked Cinema's ID
    :return: table with all Posters
    """

    if request.user.is_staff is True:
        config = RequestConfig(request)
        content = PosterTable(Poster.objects.filter(cinema_id=cinema_id))
        config.configure(content)
        return render(request, 'tables/poster/poster-table-editable.html', {
            'table': content,
        })
    else:
        return render(request, "404.html", {})


@permission_classes([AllowAny])
def form_poster_insert(request, cinema_id):
    """
    Returns Poster's insert form

    :param request:
    :param cinema_id: linked Cinema's ID
    :return: web-page for creating new entity
    """

    if request.user.is_staff is True:
        if request.method == "POST":
            form = PosterForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=True)
                instance.save()
        else:
            form = Poster.objects.filter(cinema_id=cinema_id)
        return render(request, "forms/poster/poster-insert.html", {"form": form, "films": Film.objects.all()})
    else:
        return render(request, "404.html", {})


def get_timeline_table_by_cinema_id(request, cinema_id):
    """
    Returns all Timeline entities as a table with certain Cinema's ID value

    :param request:
    :param cinema_id: linked Cinema's ID
    :return: table with all Timeline
    """

    if request.user.is_staff is True:
        config = RequestConfig(request)
        content = TimelineTable(Timeline.objects.filter(cinema_id=cinema_id))
        config.configure(content)
        return render(request, 'tables/timeline/timeline-table-editable.html', {
            'table': content,
        })
    else:
        return render(request, "404.html", {})


@permission_classes([AllowAny])
def form_timeline_insert(request, cinema_id):
    """
    Returns Timeline's insert form

    :param request:
    :param cinema_id: linked Cinema's ID
    :return: web-page for creating new entity
    """

    if request.user.is_staff is True:
        if request.method == "POST":
            form = TimelineForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=True)
                instance.save()
        else:
            form = Timeline.objects.filter(cinema_id=cinema_id)
        return render(request, "forms/timeline/timeline-insert.html", {"form": form, "films": Film.objects.all()})
    else:
        return render(request, "404.html", {})


def get_hall_table_by_cinema_id(request, cinema_id):
    """
    Returns all Hall entities as a table with certain Cinema's ID value

    :param request:
    :param cinema_id: linked Cinema's ID
    :return: table with all Hall
    """

    if request.user.is_staff is True:
        config = RequestConfig(request)
        content = HallTable(Hall.objects.filter(cinema_id=cinema_id))
        config.configure(content)
        return render(request, 'tables/hall-table.html', {
            'table': content,
        })
    else:
        return render(request, "404.html", {})


@permission_classes([AllowAny])
def form_hall_insert(request, cinema_id):
    """
    Returns Hall's insert form

    :param request:
    :param cinema_id: linked Hall's ID
    :return: web-page for creating new entity
    """

    if request.user.is_staff is True:
        if request.method == "POST":
            form = HallForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=True)
                instance.save()
        else:
            form = Hall.objects.filter(cinema_id=cinema_id)
        return render(request, "forms/hall/hall-insert.html",
                      {"form": form, "cinemas": Cinema.objects.get(pk=cinema_id),
                       "staff": Staff.objects.get(user_id=request.user.pk)})
    else:
        return render(request, "404.html", {})


@permission_classes([AllowAny])
def form_hall_update(request, cinema_id, hall_id):
    """
    Returns Hall's update form

    :param request:
    :param cinema_id: linked Cinema's ID
    :param hall_id: Hall's ID for updating
    :return: web-page for updating
    """

    if request.user.is_staff is True:
        if request.method == "POST":
            form = HallForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=True)
                instance.save()
        else:
            form = Hall.objects.filter(cinema_id=cinema_id)
        return render(request, "forms/hall/hall-update.html",
                      {"form": form, "halls": Hall.objects.get(pk=hall_id),
                       "cinemas": Cinema.objects.get(pk=cinema_id)})
    else:
        return render(request, "404.html", {})
