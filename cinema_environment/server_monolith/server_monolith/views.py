from django.shortcuts import render
from django_tables2 import RequestConfig
from django.apps import apps


def index_page(request):
    """
    Handler for Index; return page with or without Staff's data
    :param request:
    :return: index web page
    """

    my_model = apps.get_model('server_app', 'Staff')

    if request.user.pk is not None:
        return render(request, 'pages/index-unregistered-page.html',
                      {'user': request.user, 'staff': my_model.objects.get(user_id=request.user.pk)})
    else:
        return render(request, 'pages/index-unregistered-page.html')
