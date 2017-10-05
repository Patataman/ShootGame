from .helpers import *

#DIRT = load_image("assets"+os.sep+"img"+os.sep+"tiles"+os.sep+"dirt.png")
ROCK = load_image("assets"+os.sep+"img"+os.sep+"tiles"+os.sep+"rock.png")
GRASS = load_image("assets"+os.sep+"img"+os.sep+"tiles"+os.sep+"grass.png")
WATER = load_image("assets"+os.sep+"img"+os.sep+"tiles"+os.sep+"water.png")
OBSTACLE = load_image("assets"+os.sep+"img"+os.sep+"tiles"+os.sep+"obstacle.png")

TILE_WIDTH = 64
TILE_HEIGHT = 64
MAP_WIDTH = 12
MAP_HEIGHT = 12

class Tile():

    def __init__(self):
        #12x12 map
        self.tileMap = [[OBSTACLE,OBSTACLE,OBSTACLE,OBSTACLE,OBSTACLE,OBSTACLE,OBSTACLE,OBSTACLE,OBSTACLE,OBSTACLE,OBSTACLE,OBSTACLE],
                        [OBSTACLE,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,OBSTACLE],
                        [OBSTACLE,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,OBSTACLE],
                        [OBSTACLE,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,OBSTACLE],
                        [OBSTACLE,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,OBSTACLE],
                        [OBSTACLE,WATER,WATER,WATER,WATER,WATER,WATER,WATER,WATER,WATER,WATER,OBSTACLE],
                        [OBSTACLE,WATER,WATER,WATER,WATER,WATER,WATER,WATER,WATER,WATER,WATER,OBSTACLE],
                        [OBSTACLE,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,OBSTACLE],
                        [OBSTACLE,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,OBSTACLE],
                        [OBSTACLE,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,OBSTACLE],
                        [OBSTACLE,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,GRASS,OBSTACLE],
                        [OBSTACLE,OBSTACLE,OBSTACLE,OBSTACLE,OBSTACLE,OBSTACLE,OBSTACLE,OBSTACLE,OBSTACLE,OBSTACLE,OBSTACLE,OBSTACLE]]

        self.tileMap_rect = [[tile.get_rect() for tile in row] for row in self.tileMap]

    def draw(self, screen):
        for i in range(0,MAP_HEIGHT):
            for j in range(0,MAP_WIDTH):
                #centerx and centery + 32 because it's the center, not a corner
                self.tileMap_rect[j][i].centerx = 64*i+32
                self.tileMap_rect[j][i].centery = 64*j+32
                screen.blit(self.tileMap[j][i], self.tileMap_rect[j][i])

