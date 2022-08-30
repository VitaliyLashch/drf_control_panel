from django.contrib import admin
from django.urls import path
from .views import all_banners, banners_edit_content, post_banners_content, patch_banners_image, post_banners_image
urlpatterns = [
    path('banners/all', all_banners, name='all_pricee'),#метод post для отримання фільтрів
    path('banners/content', post_banners_content), #методи для post запиту данних текстових для банеру
    path('banners/content/<int:id_>', banners_edit_content), #метод для редагування і видалення данних банерів
    path('banners/image/<int:id_>', patch_banners_image), #метод для post put фотографій
    path('banners/image', post_banners_image),
]
