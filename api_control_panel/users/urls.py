from django.contrib import admin
from django.urls import path
from .views import getUserFromToken, Logout

urlpatterns = [
    path('', getUserFromToken.as_view(), name='get_user'),
    path('logout', Logout.as_view(), name='get_logout')
]