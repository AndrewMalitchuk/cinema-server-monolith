from django.apps import apps
from django.shortcuts import render


def index_page(request):
    """
    Handler for Index; return page with or without Staff's data

    :param request:
    :return: index web page
    """

    staff_model = apps.get_model('server_app', 'Staff')

    if request.user.pk is not None:
        return render(request, 'pages/index-unregistered-page.html',
                      {'user': request.user, 'staff': staff_model.objects.get(user_id=request.user.pk)})
    else:
        return render(request, 'pages/index-unregistered-page.html')


def custom_profile(request):
    """
    Handler for profile page

    :param request:
    :return: profile web-page
    """

    staff_model = apps.get_model('server_app', 'Staff')
    cinema_model = apps.get_model('server_app', 'Cinema')

    if request.user.pk is not None:
        return render(request, 'pages/profile.html',
                      {'user': request.user,
                       'staff': staff_model.objects.get(user_id=request.user.pk),
                       'cinema': cinema_model.objects.get(
                           pk=staff_model.objects.get(user_id=request.user.pk).cinema_id.id)})
    else:
        return render(request, '404.html')
