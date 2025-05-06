from django.conf import settings
from django.http import FileResponse
import os
import zipfile
BASE_DIR = settings.BASE_DIR

from django.apps import AppConfig


class DownloaderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'downloader'
