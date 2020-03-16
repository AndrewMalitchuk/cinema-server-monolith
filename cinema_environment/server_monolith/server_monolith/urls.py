"""server_monolith URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
from django.views.static import serve
from rest_framework_simplejwt import views as jwt_views

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('server_app.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', TemplateView.as_view(template_name='pages/logout-page.html'), name='logout-page'),
    # path('', TemplateView.as_view(template_name='pages/index-unregistered-page.html'),
    #      name='home'),
    path('', index_page),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
