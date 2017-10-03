# -*- coding: utf-8 -*-

import sys, os
from pygame import image, error, font
#from pygame.locals import *

# Funciones
# ---------------------------------------------------------------------
#Load image. filename: image path
def load_image(filename):
    #try to load the image
    try:
        imageFile = image.load(resource_path(filename))
    #errors
    except error:
        raise ImportError
    return imageFile

def resource_path(relative):
    application_path = os.path.abspath(".")
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the pyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app 
        # path into variable _MEIPASS'.
        application_path = sys._MEIPASS

    return os.path.join(application_path, relative)