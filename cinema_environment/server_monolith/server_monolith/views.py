from django.shortcuts import render
from django_tables2 import RequestConfig
from django.apps import apps



def index_page(request):

    MyModel = apps.get_model('server_app', 'Staff')

    return render(request, 'pages/index-unregistered-page.html', {'user':request.user,'staff':MyModel.objects.get(user_id=request.user.pk) })
