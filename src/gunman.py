from pygame import sprite
from pygame.locals import *
from .helpers import *

class Gunman(sprite.Sprite):
	def __init__(self, num, device):
		sprite.Sprite.__init__(self)
		#self.name = jsonObject['name']
		self.device = device
		self.sprites = self.load_sprites("assets/img/sprites/BuffSpriteTT.png", 64, 64)
		#self.avatar = [load_image(jsonObject['avatar']),
		#                load_image(jsonObject['avatarAlt'])]
		self.keyMap = {}
		self.bang = None # the shoot
		self.current_frame = 0
		self.setPlayer(num, device)
		self.restart()

	def restart(self):
		#Reiniciar atributos del personaje
		self.state = "idle"
		self.health = 100
		# Hacia donde mira (0 -> derecha, 4 -> izquierda)
		self.orientacion = 0
		self.x = 768/2         #X inicial
		self.y = 768/4        #Y inicial
		self.cdShoot = 0
		# Atributos necesario para calcular colisiones entre sprites
		self.image = None 
		self.rect = None

	def setPlayer(self, num, device):
		if device == "keyboard":
			self.keyMap["up"] = K_w if num == 1 else K_UP
			self.keyMap["down"] = K_s if num == 1 else K_DOWN
			self.keyMap["left"] = K_a if num == 1 else K_LEFT
			self.keyMap["right"] = K_d if num == 1 else K_RIGHT
			self.keyMap["shoot_left"] = K_c if num == 1 else K_i
			self.keyMap["shoot_head-on"] = K_v if num == 1 else K_o
			self.keyMap["shoot_right"] = K_b if num == 1 else K_p
		#elif device == "pad":
		#    self.keyMap["up"] = (0,1)
		#    self.keyMap["down"] = (0,-1)
		#    self.keyMap["left"] = (-1,0)
		#    self.keyMap["right"] = (0,1)
		#    self.keyMap["weakAttack"] = 2       #Number of the button (X on Xbox controller)
		#    self.keyMap["strongAttack"] = 3     #Number of the button (Y on Xbox controller)

	def load_sprites(self, filename, width, height):
		ficha = {}

		sprite_ficha = load_image(filename)
		ficha["front"] = []
		ficha["frontAttack"] = []
		ficha["back"] = []
		#ficha["sufferFront"] = []
		#ficha["sufferBack"] = []
		for i in range(0,3):
			ficha["front"].append(sprite_ficha.subsurface((i*64, 0*64, width, height)))
			ficha["frontAttack"].append(sprite_ficha.subsurface((i*64, 1*64, width, height)))
			ficha["back"].append(sprite_ficha.subsurface((i*64, 2*64, width, height)))

		ficha["sufferFront"] = sprite_ficha.subsurface((0, 3*64, width, height))
		ficha["sufferBack"] = sprite_ficha.subsurface((64, 3*64, width, height))

		return ficha

	def getFrame(self):
		sprite = None
		if self.current_frame == 20:
			self.current_frame = 0
		if self.cdShoot > 3:
			if self.current_frame < 5:
				sprite = self.sprites["frontAttack"][0]
			if (self.current_frame >= 5 and self.current_frame <= 10) or (self.current_frame >= 15 and self.current_frame < 20):
				sprite = self.sprites["frontAttack"][1]
			if self.current_frame >= 10 and self.current_frame < 15:
				sprite = self.sprites["frontAttack"][2]
		else:
			if self.current_frame < 5:
				sprite = self.sprites["front"][0]
			if (self.current_frame >= 5 and self.current_frame < 10) or (self.current_frame >= 15 and self.current_frame < 20):
				sprite = self.sprites["front"][1]
			if self.current_frame >= 10 and self.current_frame < 15:
				sprite = self.sprites["front"][2]
		return sprite


	# Actions
	def move(self, direction, time):
		"""El avance del personaje está definido por su orientación y límitado por su posición o estado.
		No podrá salirse de los límites del escenario.
		No podrá avanzar si está ejecutando otra acción que no sea salto.
		"""
		espacio = 0.5
		if direction == "left":
			if self.x <= 65: # PONER EL LIMITE DE MITAD DE ESCENARIO
				self.x -= time*espacio
		if direction == "up":
			if (self.y >= 65 and self.y <= 768/2) or (self.y >= 768/2 and self.y <= 768-65): # PONER EL LIMITE DE MITAD DE ESCENARIO
				self.y -= time*espacio
		if direction == "right":
			if self.x <= 768-65: # No estamos en los límites del escenario
				self.x += min(time*espacio,768-65)
		if direction == "down":
			if (self.y >= 65 and self.y <= 768/2) or (self.y >= 768/2 and self.y <= 768-65): # PONER EL LIMITE DE MITAD DE ESCENARIO
				self.y += time*espacio

	def shoot(self, direction):
		if not self.cdShoot:
			if direction == "left":
				self.bang = ((self.x, self.y+35),(-0.70,-1)) # 0.7 is sen and cos of 45º
			if direction == "head-on":
				self.bang = ((self.x, self.y+35),(0,-1))
			if direction == "right":
				self.bang = ((self.x, self.y+35),(0.70,-1))
			self.cdShoot = 6


	def actionKeyboard(self, keys, time):
		if keys[self.keyMap["right"]]:
			self.move("right", time)
		if keys[self.keyMap["left"]]:
			self.move("left", time)
		if keys[self.keyMap["up"]]:
			self.move("up", time)
		if keys[self.keyMap["down"]]:
			self.move("down", time)
		if keys[self.keyMap["shoot_left"]]:
			self.shoot("left")
		if keys[self.keyMap["shoot_head-on"]]:
			self.shoot("head-on")
		if keys[self.keyMap["shoot_right"]]:
			self.shoot("right")

	def update(self):
		##### Se calculan los atributos necesarios para las colisiones. Da igual si es 0 o 1, ya que sólo varía el color
		self.image = self.getFrame()
		self.rect = self.image.get_rect()
		self.rect.center = (self.x, self.y)
		#####

		# Actualizamos frames
		self.current_frame += 1
		self.cdShoot = max(0,self.cdShoot-1)
