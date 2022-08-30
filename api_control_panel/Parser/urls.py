from django.contrib import admin
from django.urls import path
from .views import allPrice, link, deleteLink
urlpatterns = [
path('price/all', allPrice, name='all_pricee'),
path('link', link),
path('link/<int:id_>', deleteLink)
]