import pygame
import math
from box import box
vec = pygame.math.Vector2

class button(box):

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