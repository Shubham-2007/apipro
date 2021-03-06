from django.apps import AppConfig
from django.conf import settings
import html
import pathlib
import os
from pathlib import Path
import keras
import tensorflow
from keras.models import load_model

class FileAppConfig(AppConfig):
    name = 'file_app'
    digitmodel = load_model('digitdemo1.h5')