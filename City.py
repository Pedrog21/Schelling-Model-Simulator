import numpy as np
import pygame
import random as rnd
import math
vec = pygame.math.Vector2

class city:

	def __init__(self, size, percentages, empty_percent, n_traits=2, min_rate=0.3, max_rate=1):

		self.running = False
		self.square_size = 15
		self.square = pygame.Surface([self.square_size, self.square_size])
		self.empty_colour = (255, 255, 255)
		self.border = 1
		self.border_colour = (0, 0, 0)
		self.empty_colour = (255, 255, 255)
		self.trait1_colour = (0, 0, 255)
		self.trait2_colour = (255, 0, 0)

		self.rows = size[0]
		self.cols = size[1]
		self.city_grid = np.zeros((self.rows, self.cols))
		self.percentages = percentages
		self.empty_percent = empty_percent
		self.n_traits = n_traits
		self.min_rate = min_rate
		self.max_rate = max_rate

		self.running = True

		total_dim = self.rows*self.cols
		raw_index = np.arange(total_dim)
		n_empty = math.floor(self.empty_percent*total_dim)
		n_t1 = math.floor((total_dim - n_empty)*self.percentages[0])
		n_t2 = total_dim - n_empty - n_t1

		for i in range(n_empty):
			rnd_index = rnd.randint(0, len(raw_index)-1)
			value = raw_index[rnd_index]
			raw_index = np.delete(raw_index, rnd_index)
			position = self.gen_index(value)
			self.city_grid[position[0],position[1]] = 0

		for i in range(n_t1):
			rnd_index = rnd.randint(0, len(raw_index)-1)
			value = raw_index[rnd_index]
			raw_index = np.delete(raw_index, rnd_index)
			position = self.gen_index(value)
			self.city_grid[position[0],position[1]] = 1

		for i in range(n_t2):
			rnd_index = rnd.randint(0, len(raw_index)-1)
			value = raw_index[rnd_index]
			raw_index = np.delete(raw_index, rnd_index)
			position = self.gen_index(value)
			self.city_grid[position[0],position[1]] = 2


	def draw(self, window):
		x0 = 20
		y0 = 20

		for i in range(self.rows):
			for j in range(self.cols):
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

	def gen_index(self, value):
		x = math.floor(value/self.cols)
		y = value%self.cols

		return [x, y]


	#def update(self):
