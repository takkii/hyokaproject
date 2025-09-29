import os
from os.path import dirname, join

import bakachon as baka
from django.apps import AppConfig
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

PCI = os.environ.get("picture_images")
BCF = os.environ.get("bakachon_folder")


class HyokappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hyokapp'

    def ready(self):
        baka.pull_down_a_shutter(str(PCI), str(BCF))
