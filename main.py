import pygame, os
from pygame.locals import *
from src.tile import Tile
from src.gunman import Gunman
from src.bullet import Bullet

bullets = pygame.sprite.Group()
player1 = Gunman(1, "keyboard", "assets"+os.sep+"img"+os.sep+"sprites"+os.sep+"BuffSpriteTT.png", 768/2, 768/4)
player2 = Gunman(2, "keyboard", "assets"+os.sep+"img"+os.sep+"sprites"+os.sep+"PinguSpriteTT.png", 768/2, 768-768/4)
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
        #Si se está pausado
        #if self.inMenu != 2 and self.inMenu != 3:
        #    # Se selecciona escape para el menú
        #    if keys[K_ESCAPE] and self.inMenu == 0:
        #        self.inMenu = 2

        # Controles Player1

        player1.actionKeyboard(keys, time)
        player2.actionKeyboard(keys, time)

            # Controles Player2
            #if self.player2.device == "keyboard":
            #    self.player2.actionKeyboard(keys, time, self.inMenu, self.player1)
            #else:
            #    self.player2.actionGamepad(self.pad2, time, self.inMenu, self.player1)


def on_update(time):
    player1.update()
    player2.update()

    if player1.bang:
        bullets.add(Bullet(player1.bang[0], player1.bang[1]))
        player1.bang = None

    if player2.bang:
        bullets.add(Bullet(player2.bang[0], player2.bang[1]))
        player2.bang = None

    bullets.update()

def on_draw(window, tileMap):
    window.fill((0, 0, 0))
    tileMap.draw(window)
    for bullet in bullets:
        window.blit(bullet.image, bullet.rect)
    #bullets.draw(window)
    window.blit(player1.image, player1.rect)
    window.blit(player2.image, player2.rect)


    #screen.blit(img, img_rect)


#Main function
if __name__ == '__main__':
    pygame.init()
    loop()
