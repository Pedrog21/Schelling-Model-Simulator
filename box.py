import pygame
import math
vec = pygame.math.Vector2

class box():

	def __init__ (self, x, y, width, height, border=0, border_colour=(0,0,0)):

		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.pos = vec(x, y)
		self.title_pos = vec(x, y - 20)
		self.size = vec(width, height)
		self.border = border
		self.border_colour = border_colour
		self.active = False

	def update(self):
		pass

	def draw(self):
		pass

	def check_click(self, pos):
		if pos[0] > self.x and pos[0] < self.x + self.width:
			if pos[1] > self.y and pos[1] < self.y + self.height:
				self.active = True
			else:
				self.active = False
		else:
			self.active = False
	