# -*- coding: utf-8 -*-

from pygame import sprite
from pygame.locals import *
from helpers import *

class Bullet(sprite.Sprite):
	def __init__(self, position, vector):
		sprite.Sprite.__init__(self)
		#self.name = jsonObject['name']
		self.image = load_image("assets/img/sprites/Bullet.png")
		self.rect = None
		self.x = position[0]
		self.y = position[1]
		self.vector = vector

	def move(self):
		"""El avance del personaje está definido por su orientación y límitado por su posición o estado.
		No podrá salirse de los límites del escenario.
		No podrá avanzar si está ejecutando otra acción que no sea salto.
		"""
		espacio = 15
		self.x += espacio*self.vector[0]
		self.y += espacio*self.vector[1]

	def update(self):
		##### Se calculan los atributos necesarios para las colisiones. Da igual si es 0 o 1, ya que sólo varía el color
		self.move()
		self.rect = self.image.get_rect()
		self.rect.center = (self.x, self.y)
