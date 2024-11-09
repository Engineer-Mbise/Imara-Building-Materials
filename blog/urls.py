from django.urls import path

from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.index, name="index"),
    path("mabati", views.mabati, name="mabati"),
    path("place_order/<str:name>/", views.place_order, name="place_order"),
]
