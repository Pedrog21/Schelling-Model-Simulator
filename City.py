import numpy as np
import pygame
vec = pygame.math.Vector2

#size is an array [a, b] where a is the width and b is the length of the city grid
class city:

	def __init__(self, size):
		self.width = size[0]
		self.height = size[1]
		self.city_grid = np.zeros((self.width, self.height))

		self.city_grid[:,0] = np.ones(self.width)
		self.city_grid[:,1] = 2*np.ones( self.width)

		self.square_size = 15
		self.square = pygame.Surface([self.square_size, self.square_size])
		self.empty_colour = (255, 255, 255)
		self.trait1_colour = (0, 0, 255)
		self.trait2_colour = (255, 0, 0)
		self.border = 1
		self.border_colour = (0, 0, 0)


	def draw(self, window):
		x0 = 20
		y0 = 20

		for i in range(self.width):
			for j in range(self.height):
				self.square.fill(self.border_colour)
				if self.city_grid[i, j] == 0:
					pygame.draw.rect(self.square, self.empty_colour, 
						(self.border/2, self.border/2, self.square_size-self.border, self.square_size-self.border))
				elif self.city_grid[i, j] == 1:
					pygame.draw.rect(self.square, self.trait1_colour, 
						(self.border/2, self.border/2, self.square_size-self.border, self.square_size-self.border))
				else:
					pygame.draw.rect(self.square, self.trait2_colour, 
						(self.border/2, self.border/2, self.square_size-self.border, self.square_size-self.border))

				pos = vec(x0 + i*self.square_size - self.border, y0 + j*self.square_size - self.border)
				window.blit(self.square, pos)
