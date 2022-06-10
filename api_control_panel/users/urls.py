from django.contrib import admin
from django.urls import path, re_path
from .views import User, Logout
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')
urlpatterns = [

    path('', User.as_view(), name='get_user'),
    path('logout', Logout.as_view(), name='get_logout'),

]