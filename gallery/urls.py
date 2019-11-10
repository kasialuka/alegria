from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import GalleryListView, GalleryDetailView
from django.conf import settings

from django.conf.urls.static import static

app_name = 'comida'

urlpatterns = [
    path(r'', GalleryListView.as_view(), name='gallery-list'),
    url(r'^gallery/(?P<pk>\d+)/$', GalleryDetailView.as_view(), name='gallery-detail'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

