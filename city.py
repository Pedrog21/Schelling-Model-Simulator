import numpy as np
import pygame
import random as rnd
import math
vec = pygame.math.Vector2

class city:

	def __init__(self, size, percentages, empty_percent, n_traits=2, min_rate=0.3, max_rate=1, max_iter=3000):

		self.max_iter = max_iter
		self.square_size = 15
		self.square = pygame.Surface([self.square_size, self.square_size])
		self.empty_colour = (255, 255, 255)
		self.border = 1
		self.border_colour = (0, 0, 0)
		self.empty_colour = (255, 255, 255)
		self.n_traits = n_traits
		colours = [(168, 0, 0), (6, 52, 62), (6, 52, 158), (101, 177, 0), (82, 111, 158), (108, 73, 4), (49, 14, 18), (2, 52, 3), (246, 250, 3)]
		self.trait_colours = colours[:self.n_traits]

		self.rows = int(size[0])
		self.cols = int(size[1])
		self.city_grid = np.zeros((self.rows, self.cols))
		self.percentages = percentages
		self.empty_percent = empty_percent
		self.min_rate = min_rate
		self.max_rate = max_rate
		self.empty = np.array([])
		self.empty.astype(int)

		self.update_iter = 0
		self.running = True

		self.total_dim = self.rows*self.cols
		raw_index = np.arange(self.total_dim)
		n_empty = math.floor(self.empty_percent*self.total_dim)
		n_trait_individuals = []
		for i in range(n_traits - 1):
			n_trait_individuals += [math.floor((self.total_dim - n_empty)*self.percentages[i])]
		n_trait_individuals += [self.total_dim - sum(n_trait_individuals) - n_empty]

		for i in range(n_empty):
			rnd_index = rnd.randint(0, len(raw_index)-1)
			value = raw_index[rnd_index]
			self.empty = np.append(self.empty, raw_index[rnd_index])
			raw_index = np.delete(raw_index, rnd_index)
			position = self.gen_index(value)
			self.city_grid[position[0],position[1]] = 0			

		for z in range(self.n_traits):
			for i in range(n_trait_individuals[z]):
				rnd_index = rnd.randint(0, len(raw_index)-1)
				value = raw_index[rnd_index]
				raw_index = np.delete(raw_index, rnd_index)
				position = self.gen_index(value)
				self.city_grid[position[0],position[1]] = z + 1

		self.unhappy = np.array([])
		self.unhappy.astype(int)

		self.set_unhappy()

	def draw(self, window):
		x0 = 20
		y0 = 20

		for i in range(self.rows):
			for j in range(self.cols):
				self.square.fill(self.border_colour)
				if self.city_grid[i, j] == 0:
					pygame.draw.rect(self.square, self.empty_colour, 
						(self.border, self.border, self.square_size-self.border*2, self.square_size-self.border*2))
				else:
					pygame.draw.rect(self.square, self.trait_colours[int(self.city_grid[i, j]) - 1], 
						(self.border, self.border, self.square_size-self.border*2, self.square_size-self.border*2))

				pos = vec(x0 + i*self.square_size - self.border/2, y0 + j*self.square_size - self.border/2)
				window.blit(self.square, pos)

	def update(self):
		if len(self.unhappy > 0) and self.update_iter <= self.max_iter:
			rnd_index_empty = rnd.randint(0,len(self.empty)-1)
			index_empty_processed = self.gen_index(self.empty[rnd_index_empty])
			rnd_index_unhappy = rnd.randint(0,len(self.unhappy)-1)
			index_unhappy_processed = self.gen_index(self.unhappy[rnd_index_unhappy])
			value = self.city_grid[index_unhappy_processed[0], index_unhappy_processed[1]]

			self.empty = np.append(self.empty, self.unhappy[rnd_index_unhappy])
			self.city_grid[index_unhappy_processed[0], index_unhappy_processed[1]] = 0
			self.city_grid[index_empty_processed[0], index_empty_processed[1]] = value
			self.empty = np.delete(self.empty, rnd_index_empty)

			self.unhappy = np.array([])
			self.unhappy.astype(int)
			self.set_unhappy()

			self.update_iter +=1

		else:
			self.running = False

	def gen_index(self, value):
		x = math.floor(value/self.cols)
		y = value%self.cols
		return [x, int(y)]

	def gen_raw_index(self, index):
		return int(index[0]*self.cols + index[1])
		
	def set_unhappy(self):
		for i in range(self.rows):
			for j in range(self.cols):
				if self.check_unhappy([i,j]):
					self.unhappy = np.append(self.unhappy, self.gen_raw_index([i,j]))

	def check_unhappy(self, position):
		x = position[0]
		y = position[1]
		same = 0
		different = 0
		pos = self.city_grid[x,y]

		if pos != 0:			
			for i in [-1,0,1]:
				for j in [-1,0,1]:
					if 0 <= x + i < self.rows and 0 <= y + j < self.cols and not (i == 0 and j == 0):
						neig = self.city_grid[x+i, y+j]
						if neig != 0 and pos == neig:
							same += 1
						elif neig != 0 and pos != neig:
							different += 1
			if same != 0 or different != 0:
				rate = same/(same + different)
				return rate < self.min_rate or rate > self.max_rate
			else:
				return False
		else:
			return False
