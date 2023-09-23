from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("upload/", UploadFileApiView.as_view(), name="upload_file"),
    path("files/", ListFilesApiView.as_view(), name="list_files")
]
