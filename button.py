import pygame
import math
from box import box
vec = pygame.math.Vector2

class button(box):

	def __init__ (self, x, y, width, height, text="", border=4, border_colour=(0,28,57), 
		text_size=30, bg_colour=(166,166,166), text_colour=(0,51,102), active_colour=(129,129,129), hor_space=0, ver_space=0):

		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.pos = vec(x, y)
		self.size = vec(width, height)
		self.image = pygame.Surface([width, height])
		self.hor_space = hor_space
		self.ver_space = ver_space
		self.text = text
		self.text_size = text_size
		self.text_colour = text_colour
		self.text_len = len(self.text)
		self.text_pos = vec(x + self.hor_space/2, y + self.ver_space)
		self.font = pygame.font.SysFont("times new roman", self.text_size)
		self.active_colour = active_colour
		self.border = border
		self.border_colour = border_colour
		self.active = False
		self.bg_colour = bg_colour

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
		text_surface = self.font.render(self.text, False, self.text_colour)
		window.blit(text_surface, self.text_pos)


	def deactivate(self):
		self.active = False

	def activate(self):
		self.active = True
