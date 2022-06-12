from django.contrib import admin
from django.urls import path
from .views import loger_api_filters, loger_traceback_filters
urlpatterns = [
    path('api_record', loger_api_filters, name='get_user'),
    path('traceback_record', loger_traceback_filters, name='get_user')
]
