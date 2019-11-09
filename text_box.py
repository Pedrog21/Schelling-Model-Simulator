import pygame
vec = pygame.math.Vector2

class text_box():

	def __init__(self, x, y, width, height, colour=(255, 255, 255)):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.pos = vec(x, y)
		self.size = vec(width, height)
		self.image = pygame.Surface(width, height)
		self.colour = colour

	def draw(self, window):
		self.image.fill(self.colour)
		window.blit(self.image, self.pos)