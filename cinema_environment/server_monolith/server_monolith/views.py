from django.shortcuts import render
from django_tables2 import RequestConfig


def index_page(request):
    print(request.user.is_staff)
    return render(request, 'pages/index-unregistered-page.html', {'user':request.user })
