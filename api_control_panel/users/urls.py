from django.contrib import admin
from django.urls import path
from .views import getUserFromToken, Logout

urlpatterns = [
    path('user', getUserFromToken.as_view(), name='get_user'),
    path('user/logout', Logout.as_view(), name='get_logout')
]