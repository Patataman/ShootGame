import sys, os
from pygame import image, error, font

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

def draw_text(text, posx, posy, size=25, color=(255, 255, 255)):
    fuente = font.Font(resource_path("assets"+os.sep+"fonts"+os.sep+"OpenSans-Regular.ttf"), size)
    salida = fuente.render(text, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    
    return salida, salida_rect

def resource_path(relative):
    application_path = os.path.abspath(".")
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the pyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app 
        # path into variable _MEIPASS'.
        application_path = sys._MEIPASS

    return os.path.join(application_path, relative)