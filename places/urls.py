from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('place/<place_pk>/', views.get_json_place, name='get_json_place'),
]
