import numpy as np
import pygame
vec = pygame.math.Vector2

class city:

	def __init__(self):

		self.running = False
		self.square_size = 15
		self.square = pygame.Surface([self.square_size, self.square_size])
		self.empty_colour = (255, 255, 255)
		self.border = 1
		self.border_colour = (0, 0, 0)

	def set_inputs(self, size, percentages, empty_spots, n_traits=2, min_rate=0.3, max_rate=1):

		self.width = size[0]
		self.height = size[1]
		self.city_grid = np.zeros((self.width, self.height))
		self.percentages = percentages
		self.empty_spots = empty_spots
		self.n_traits = n_traits
		self.min_rate = min_rate
		self.max_rate = max_rate

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

	def run(self):

		self.running = True
		

	def update(self):
