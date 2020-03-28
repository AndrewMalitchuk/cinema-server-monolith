import qrcode
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from django_tables2 import SingleTableView, RequestConfig
from django_tables2.export import ExportMixin, TableExport
from qrcode.image.pure import PymagingImage
from rest_framework import status, permissions
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from qrcode.image.pure import PymagingImage

from .tables import *
from .forms import *
from .permission import IsStaffOrAdminWriteOnly
from .serializers import *


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsStaffOrAdminWriteOnly])
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
@permission_classes([IsStaffOrAdminWriteOnly])
def api_timeline(request):
    if request.method == 'GET':
        timeline = Timeline.objects.all()
        serializer = TimelineSerializer(timeline, many=True)

        cinema_id = request.GET.get('cinema_id', None)
        film_id = request.GET.get('film_id', None)
        id = request.GET.get('id', None)
        datetime = request.GET.get('datetime', None)

        if cinema_id is not None and film_id is not None and datetime is None:
            timeline = Timeline.objects.filter(cinema_id=cinema_id, film_id=film_id)
            serializer = TimelineSerializer(timeline, many=True)
        elif cinema_id is not None and film_id is not None and datetime is not None:
            timeline = Timeline.objects.filter(cinema_id=cinema_id, film_id=film_id, datetime=datetime)
            serializer = TimelineSerializer(timeline, many=True)
        elif cinema_id is not None and film_id is None and datetime is None:
            timeline = Timeline.objects.filter(cinema_id=cinema_id)
            serializer = TimelineSerializer(timeline, many=True)
        elif cinema_id is None and film_id is not None and datetime is None:
            timeline = Timeline.objects.filter(film_id=film_id)
            serializer = TimelineSerializer(timeline, many=True)
        elif cinema_id is None and film_id is None and datetime is not None:
            timeline = Timeline.objects.filter(datetime=datetime)
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
@permission_classes([IsStaffOrAdminWriteOnly])
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
@permission_classes([IsStaffOrAdminWriteOnly])
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
@permission_classes([IsStaffOrAdminWriteOnly])
def get_staff_job(request):
    if request.method == 'GET':
        user_id=request.GET.get('user_id',None)
        if user_id is not None:
            staff=Staff.objects.get(user_id=user_id)
            cinema=Cinema.objects.get(pk=staff.cinema_id.id)
            serializer=CinemaSerializer(cinema,many=False)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
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
    # permission_classes = (IsAuthenticated,)
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]

    serializer_class = UserSerializer


#
@permission_classes([AllowAny])
def hall_form(request):
    if request.method == "POST":
        form = HallForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=True)
            instance.save()
    else:
        form = HallForm()
    return render(request, "forms/hall_form.html", {"form": form})





@permission_classes([AllowAny])
def cinema_profile(request, cinema_id):
    form = Cinema.objects.get(pk=cinema_id)
    return render(request, "pages/cinema-profile.html", {"form": form})


@permission_classes([AllowAny])
def about_film(request, film_id):
    form = Film.objects.get(pk=film_id)
    return render(request, "pages/about-film.html", {"form": form})





# Email sending test
@api_view(['GET'])
@permission_classes([AllowAny])
def email(request):
    if request.method == 'GET':
        email = request.GET.get('email', None)
        if email is not None:

            # https://pypi.org/project/qrcode/
            # https://dropmail.me/ru/

            subject = 'cinema-app'
            body = 'Here is your ticket, comrade'
            from_email = settings.EMAIL_HOST_USER
            to_email = email

            mail = EmailMessage(subject=subject, body=body, from_email=from_email, to=[to_email])

            qr = qrcode.QRCode()
            qr.add_data('test text')
            qr.make()
            img = qr.make_image(fill_color="#D81B60", back_color="white")
            img.save('/home/adular/QR/ticket.png')

            mail.attach_file('/home/adular/QR/ticket.png')
            mail.send(fail_silently=True)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class FilmTableView(ExportMixin, SingleTableView):
    model = Film
    table_class = FilmTable
    template_name = 'tables/film-table.html'


# Cinema Web
def cinema_table_all(request):
    config = RequestConfig(request)

    print(request.user.is_staff)

    if request.user.is_staff == True:
        content = CinemaTableEditable(Cinema.objects.all())

        config.configure(content)
        return render(request, 'tables/cinema/cinema-table-editable.html', {
            'table': content,
        })
    else:
        content = CinemaTableUneditable(Cinema.objects.all())

        config.configure(content)
        return render(request, 'tables/cinema/cinema-table-uneditable.html', {
            'table': content,
        })


@permission_classes([AllowAny])
def form_cinema_udpate(request, cinema_id):
    if request.user.is_staff == True:
        if request.method == "POST":
            form = CinemaForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=True)
                instance.save()
        else:
            form = Cinema.objects.get(pk=cinema_id)
        return render(request, "forms/cinema/cinema-update.html", {"form": form})
    else:
        return render(request, "404.html", {})


@permission_classes([AllowAny])
def form_cinema_insert(request):
    if request.user.is_staff == True:
        if request.method == "POST":
            form = CinemaForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=True)
                instance.save()
        else:
            form = CinemaForm()
        return render(request, "forms/cinema/cinema-insert.html", {"form": form})
    else:
        return render(request, "404.html", {})


# Poster Web
def get_poster_table_by_cinema_id(request, cinema_id):
    if request.user.is_staff == True:
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
    if request.user.is_staff == True:
        if request.method == "POST":
            form = PosterForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=True)
                instance.save()
        else:
            form = Poster.objects.filter(cinema_id=cinema_id)
            data = Film.objects.all()
        return render(request, "forms/poster/poster-insert.html", {"form": form, "films": Film.objects.all()})
    else:
        return render(request, "404.html", {})

# Timeline Web
def get_timeline_table_by_cinema_id(request, cinema_id):
    if request.user.is_staff == True:
        config = RequestConfig(request)
        content = TimelineTable(Timeline.objects.filter(cinema_id=cinema_id))

        config.configure(content)

        return render(request, 'tables/timeline-table-editable.html', {
            'table': content,
        })
    else:
        return render(request, "404.html", {})

# TODO: permission
@permission_classes([AllowAny])
def form_timeline_insert(request, cinema_id):
    if request.user.is_staff == True:
        if request.method == "POST":
            form = TimelineForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=True)
                instance.save()
        else:
            form = Timeline.objects.filter(cinema_id=cinema_id)
            data = Film.objects.all()
        return render(request, "forms/timeline/timeline-insert.html", {"form": form, "films": Film.objects.all()})
    else:
        return render(request, "404.html", {})

# Hall Web
def get_hall_table_by_cinema_id(request, cinema_id):
    if request.user.is_staff == True:
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
    if request.user.is_staff == True:
        if request.method == "POST":
            form = HallForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=True)
                instance.save()
        else:
            form = Hall.objects.filter(cinema_id=cinema_id)
        return render(request, "forms/hall/hall-insert.html", {"form": form, "cinemas": Cinema.objects.get(pk=cinema_id)})
    else:
        return render(request, "404.html", {})

@permission_classes([AllowAny])
def form_hall_update(request, cinema_id, hall_id):
    if request.user.is_staff == True:
        if request.method == "POST":
            form = HallForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=True)
                instance.save()
        else:
            form = Hall.objects.filter(cinema_id=cinema_id)
        return render(request, "forms/hall/hall-update.html",
                      {"form": form, "halls": Hall.objects.get(pk=hall_id), "cinemas": Cinema.objects.get(pk=cinema_id)})
    else:
        return render(request, "404.html", {})

def get_ticket_table_by_cinema_id(request, cinema_id):
    config = RequestConfig(request)
    content = TicketTable(Ticket.objects.filter(cinema_id=cinema_id))

    config.configure(content)

    return render(request, 'tables/ticket_table.html', {
        'table': content,
    })


def get_ticket_table_by_cinema_id_and_film_id(request, cinema_id, film_id):
    config = RequestConfig(request)
    content = TicketTable(Ticket.objects.filter(cinema_id=cinema_id, film_id=film_id))

    config.configure(content)

    return render(request, 'tables/ticket_table.html', {
        'table': content,
    })











# XXX
@api_view(['GET'])
@permission_classes([AllowAny])
def table_view(request):
    # XXX
    # TODO: 1. for certain table; 2. only to allowed table;
    if request.method == 'GET':
        table = request.GET.get('table', None)
        format = request.GET.get('format', None)

        if table is None or format is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            table = FilmTable(Film.objects.all())

            RequestConfig(request).configure(table)

            export_format = request.GET.get("_export", None)
            if TableExport.is_valid_format(export_format):
                exporter = TableExport(export_format, table)
                return exporter.response("table.{}".format(export_format))

            return render(request, "forms/film_list.html", {
                "table": table
            })

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


