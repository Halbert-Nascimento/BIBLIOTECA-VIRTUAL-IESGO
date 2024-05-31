from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('listbooks/', views.list_books, name='list_books'),
    path('bookregister/', views.book_register, name='book_register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
