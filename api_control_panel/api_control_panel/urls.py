"""api_control_panel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from django.views.generic import TemplateView
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Pastebin API')
urlpatterns = [
    path('users/', include('users.urls'), name='token_verify'),
    re_path(r'^$', schema_view),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('logger/', include('logger.urls')),
    path('telegram_bot/', include('telegram_bot.urls')),
    path('parser/', include('Parser.urls')),
    path('mobileapp/', include('mobileapp.urls')),
    path('collector/', include('collector.urls')),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'schema.yml'}
    ), name='swagger-ui')
]
schema_view = get_swagger_view(title='Pastebin API')