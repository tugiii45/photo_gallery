from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.register, name="register"),
    path("photo/<int:photo_id>/", views.photo_detail, name="photo_detail"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("", views.home, name="home"),
]