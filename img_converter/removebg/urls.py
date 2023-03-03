from django.urls import path

from .views import index, download_file


app_name = "remove-bg"
urlpatterns = [
    path("", index, name="remove-bg-index"),
    path("download/<file>/<filename>", download_file, name="remove-bg-download"),
]
