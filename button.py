import pygame
import math
from box import box
vec = pygame.math.Vector2

class button(box):

	def __init__ (self, x, y, width, height, text="", border=0, border_colour=(0,0,0), text_size=12):

		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.pos = vec(x, y)
		self.title_pos = vec(x, y - 20)
		self.size = vec(width, height)
		self.image = pygame.Surface([width, height])
		self.text = text
		self.text_size = text_size
		self.border = border
		self.border_colour = border_colour
		self.active = False

	#def draw(self, window):

	def deactivate(self):
		self.active = False
