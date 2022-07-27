from django.urls import path

from .views import download_file, index, login_user, logout_user, register

app_name = "main"
urlpatterns = [
    path("", index, name="index"),
    path("download/<file>/<filename>", download_file, name="download"),
    path("register", register, name="register"),
    path("login_user", login_user, name="login_user"),
    path("logout_user", logout_user, name="logout_user"),
]
