from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_json_place/<place_pk>', views.get_json_place, name='get_json_place'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
