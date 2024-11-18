from django.urls import path

from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("registration/", views.registration, name="registration"),
    path("login/",views.login_view,name="login"),
    path("logout/",views.user_logout,name="logout"),
]