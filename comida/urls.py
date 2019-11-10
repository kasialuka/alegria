from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import FoodDetailView, FoodListView
from django.conf import settings

from django.conf.urls.static import static

app_name = 'comida'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', FoodListView.as_view(), name='food-list'),
    url(r'^product/(?P<pk>\d+)/$', FoodDetailView.as_view(), name='food-detail'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

