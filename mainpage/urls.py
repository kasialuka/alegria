from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import HeaderView, FooterView
from django.conf import settings

from django.conf.urls.static import static

app_name = 'mainpage'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', HeaderView.as_view(), name='footer'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

