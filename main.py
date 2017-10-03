# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from src.tile import Tile

#Game itself
def loop():
    #------------- Init -------------
    #Display a window of 768x768
    window = pygame.display.set_mode([768,768])
    #Window name
    pygame.display.set_caption("ShootGame")
    #Variables
    quit_flag = False
    clock = pygame.time.Clock()
    tileMap = Tile()
    #Options
    pygame.key.set_repeat(10, 200)
    #--------------------------------

    while not quit_flag:
        time = clock.tick(30)

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_flag = True

            # detect events
            on_event(time, event)

        # update scene (stuff)
        on_update(time)

        # redraw the screen
        on_draw(window, tileMap)
        pygame.display.flip()

#on_event function, 
def on_event(time, event):
    pass

def on_update(time):
    pass

def on_draw(window, tileMap):
    window.fill((0, 0, 0))
    tileMap.draw(window)

    #screen.blit(img, img_rect)


#Main function
if __name__ == '__main__':
    pygame.init()
    loop()
