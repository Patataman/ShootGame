import pygame, os
from pygame.locals import *
from src.tile import Tile
from src.gunman import Gunman
from src.bullet import Bullet
from src.helpers import *

bullets = pygame.sprite.Group()
player1 = Gunman(1, "keyboard", "assets"+os.sep+"img"+os.sep+"sprites"+os.sep+"BuffSpriteTT.png", 768/2, 768/4)
player2 = Gunman(2, "keyboard", "assets"+os.sep+"img"+os.sep+"sprites"+os.sep+"PinguSpriteTT.png", 768/2, 768-768/4)
countdown = 91 #Combat time

#Game itself
def loop():
    #------------- Init -------------
    #Display a window of 768x768
    window = pygame.display.set_mode([832,768])

    #Window name
    pygame.display.set_caption("ShootGame")

    #Variables
    quit_flag = False
    clock = pygame.time.Clock()
    tileMap = Tile()
    #Options
    pygame.key.set_repeat(10, 200)
    #Characters

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
    if pygame.KEYDOWN:
        keys = pygame.key.get_pressed()

        # Controles Player1
        player1.actionKeyboard(keys, time)

        # Controles Player2
        player2.actionKeyboard(keys, time)

def on_update(time):
    if countdown > 0:

        player1.update()
        player2.update()

        global countdown
        countdown -= time/1000

        if player1.bang:
            bullets.add(Bullet(player1.bang[0], player1.bang[1]))
            player1.bang = None

        if player2.bang:
            bullets.add(Bullet(player2.bang[0], player2.bang[1]))
            player2.bang = None

        bullets.update()

    elif countdown <= 0:
        pass

def on_draw(window, tileMap):
    window.fill((0, 0, 0))
    tileMap.draw(window)
    for bullet in bullets:
        window.blit(bullet.image, bullet.rect)

    timeCD, time_rect = draw_text(str(int(countdown)), 768+32, 768/2, 30)
    window.blit(timeCD, time_rect)
    window.blit(player1.image, player1.rect)
    window.blit(player2.image, player2.rect)
    for heart in player1.heart:
        window.blit(heart[0], heart[1])
    for heart in player2.heart:
        window.blit(heart[0], heart[1])

#Main function
if __name__ == '__main__':
    pygame.init()
    loop()
