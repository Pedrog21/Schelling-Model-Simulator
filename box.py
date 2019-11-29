import pygame
import math
vec = pygame.math.Vector2

class box():

	def __init__ (self, x, y, width, height, border=0, border_colour=(166,0,0), bg_colour=(166,0,0)):

		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.pos = vec(x, y)
		self.title_pos = vec(x, y - 20)
		self.image = pygame.Surface([self.width, self.height])
		self.size = vec(width, height)
		self.border = border
		self.border_colour = border_colour
		self.bg_colour = bg_colour
		self.active = False

	def update(self):
		pass

	def draw(self, window):
		if self.border == 0:
			if self.active:
				self.image.fill(self.active_colour)
			else:
				self.image.fill(self.bg_colour)
		else:
			self.image.fill(self.border_colour)
			if self.active:
				pygame.draw.rect(self.image, self.active_colour, 
					(self.border, self.border, self.width-self.border*2, self.height-self.border*2))
			else:				
				pygame.draw.rect(self.image, self.bg_colour, 
					(self.border, self.border, self.width-self.border*2, self.height-self.border*2))

		window.blit(self.image, self.pos)

	def check_click(self, pos):
		if pos[0] > self.x and pos[0] < self.x + self.width:
			if pos[1] > self.y and pos[1] < self.y + self.height:
				self.active = True
			else:
				self.active = False
		else:
			self.active = False
	