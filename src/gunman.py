from pygame import sprite
from pygame.locals import *
from .helpers import *

class Gunman(sprite.Sprite):
	def __init__(self, num, device, filepath, posX, posY):
		sprite.Sprite.__init__(self)

		self.device = device
		self.orientation = 1 if num==1 else -1
		self.heart = []

		self.sprites = self.load_sprites(filepath, 64, 64)
		self.keyMap = {}
		self.bang = None # the shoot
		self.current_frame = 0
		self.setPlayer(num, device)
		self.restart(posX, posY)

	def restart(self, posX, posY):
		#Reiniciar atributos del personaje
		self.state = "idle"
		self.health = 5
		self.x = posX         #X inicial
		self.y = posY         #Y inicial	
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
		for i in range(0,3):
			ficha["front"].append(sprite_ficha.subsurface((i*64, 0*64, width, height)))
			ficha["frontAttack"].append(sprite_ficha.subsurface((i*64, 1*64, width, height)))
			ficha["back"].append(sprite_ficha.subsurface((i*64, 2*64, width, height)))

		ficha["sufferFront"] = sprite_ficha.subsurface((0, 3*64, width, height))
		ficha["sufferBack"] = sprite_ficha.subsurface((64, 3*64, width, height))

		for i in range(0,5):
			h = load_image("assets"+os.sep+"img"+os.sep+"heart.png")
			h_rect = h.get_rect()
			h_rect.centerx = 768+32
			if self.orientation == 1:
				h_rect.centery = 64*i + 32
			if self.orientation == -1:
				h_rect.centery = 768/2 + 64*i + 96
			self.heart.append([h, h_rect])

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
			if self.x > 115:
				self.x -= time*espacio
		if direction == "up":
			if (self.orientation == 1 and self.y > 95) or \
				(self.orientation == -1 and self.y > 768/2 + 95):
				self.y -= time*espacio
		if direction == "right":
			if self.x < 768-96:
				self.x += min(time*espacio,768-100)
		if direction == "down":
			if (self.orientation == 1 and self.y < 768/2-95) or \
				(self.orientation == -1 and self.y < 768-100):
				self.y += time*espacio

	def shoot(self, direction):
		if not self.cdShoot:
			if direction == "left":
				self.bang = ((self.x, self.y+35),(-0.70,self.orientation)) # 0.7 is sen and cos of 45º
			if direction == "head-on":
				self.bang = ((self.x, self.y+35),(0,self.orientation))
			if direction == "right":
				self.bang = ((self.x, self.y+35),(0.70,self.orientation))
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
