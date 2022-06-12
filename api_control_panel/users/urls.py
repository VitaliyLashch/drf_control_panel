from django.contrib import admin
from django.urls import path, re_path
from .views import uuser, Logout, getUserAll, settings_user
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')
urlpatterns = [

    path('', uuser.as_view(), name='get_user'),
    path('all', getUserAll, name='all_users'),
    path('settings', settings_user, name='settings'),
    path('logout', Logout.as_view(), name='get_logout'),

]