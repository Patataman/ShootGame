from .helpers import *
import random

#DIRT = load_image("assets"+os.sep+"img"+os.sep+"tiles"+os.sep+"dirt.png")
#ROCK = load_image("assets"+os.sep+"img"+os.sep+"tiles"+os.sep+"rock.png")
#GRASS = load_image("assets"+os.sep+"img"+os.sep+"tiles"+os.sep+"grass.png")
#WATER = load_image("assets"+os.sep+"img"+os.sep+"tiles"+os.sep+"water.png")
#OBSTACLE = load_image("assets"+os.sep+"img"+os.sep+"tiles"+os.sep+"obstacle.png")

BORDER1 = load_image("assets"+os.sep+"img"+os.sep+"tiles"+os.sep+"border1.png")
BORDER2 = load_image("assets"+os.sep+"img"+os.sep+"tiles"+os.sep+"border2.png")
BORDER3 = load_image("assets"+os.sep+"img"+os.sep+"tiles"+os.sep+"border3.png")
BORDER4 = load_image("assets"+os.sep+"img"+os.sep+"tiles"+os.sep+"border4.png")
GRASS1 = load_image("assets"+os.sep+"img"+os.sep+"tiles"+os.sep+"grass1.png")
GRASS2 = load_image("assets"+os.sep+"img"+os.sep+"tiles"+os.sep+"grass2.png")
GRASS3 = load_image("assets"+os.sep+"img"+os.sep+"tiles"+os.sep+"grass3.png")
WATER1 = load_image("assets"+os.sep+"img"+os.sep+"tiles"+os.sep+"water1.png")
WATER2 = load_image("assets"+os.sep+"img"+os.sep+"tiles"+os.sep+"water2.png")

BORDERS_EX = (BORDER1, BORDER2)
BORDERS_IN = (BORDER3, BORDER4)
GRASS = (GRASS1, GRASS2, GRASS3)
WATER = (WATER1, WATER2)

def borderEx():
    return BORDERS_EX[random.randrange(0, len(BORDERS_EX))]
def borderIn():
    return BORDERS_IN[random.randrange(0, len(BORDERS_IN))]
def grass():
    return GRASS[random.randrange(0, len(GRASS))]
def water():
    return WATER[random.randrange(0, len(WATER))]

TILE_WIDTH = 64
TILE_HEIGHT = 64
MAP_WIDTH = 12
MAP_HEIGHT = 12

class Tile():

    def __init__(self):
        #12x12 map
        self.tileMap = [[borderEx(),borderEx(),borderEx(),borderEx(),borderEx(),borderEx(),borderEx(),borderEx(),borderEx(),borderEx(),borderEx(),borderEx()],
                        [borderEx(),borderIn(),borderIn(),borderIn(),borderIn(),borderIn(),borderIn(),borderIn(),borderIn(),borderIn(),borderIn(),borderEx()],
                        [borderEx(),borderIn(),grass(),grass(),grass(),grass(),grass(),grass(),grass(),grass(),borderIn(),borderEx()],
                        [borderEx(),borderIn(),grass(),grass(),grass(),grass(),grass(),grass(),grass(),grass(),borderIn(),borderEx()],
                        [borderEx(),borderIn(),grass(),grass(),grass(),grass(),grass(),grass(),grass(),grass(),borderIn(),borderEx()],
                        [WATER1,WATER2,WATER1,WATER2,WATER1,WATER2,WATER1,WATER2,WATER1,WATER2,WATER1,WATER2],
                        [WATER2,WATER1,WATER2,WATER1,WATER2,WATER1,WATER2,WATER1,WATER2,WATER1,WATER2,WATER1],
                        [borderEx(),borderIn(),grass(),grass(),grass(),grass(),grass(),grass(),grass(),grass(),borderIn(),borderEx()],
                        [borderEx(),borderIn(),grass(),grass(),grass(),grass(),grass(),grass(),grass(),grass(),borderIn(),borderEx()],
                        [borderEx(),borderIn(),grass(),grass(),grass(),grass(),grass(),grass(),grass(),grass(),borderIn(),borderEx()],
                        [borderEx(),borderIn(),borderIn(),borderIn(),borderIn(),borderIn(),borderIn(),borderIn(),borderIn(),borderIn(),borderIn(),borderEx()],
                        [borderEx(),borderEx(),borderEx(),borderEx(),borderEx(),borderEx(),borderEx(),borderEx(),borderEx(),borderEx(),borderEx(),borderEx()]]

        self.tileMap_rect = [[tile.get_rect() for tile in row] for row in self.tileMap]

    def draw(self, screen):
        for i in range(0,MAP_HEIGHT):
            for j in range(0,MAP_WIDTH):
                #centerx and centery + 32 because it's the center, not a corner
                self.tileMap_rect[j][i].centerx = 64*i+32
                self.tileMap_rect[j][i].centery = 64*j+32
                screen.blit(self.tileMap[j][i], self.tileMap_rect[j][i])

