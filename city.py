import numpy as np
import pygame
import random as rnd
import math
from button import button
from box import box
vec = pygame.math.Vector2

class city:

	def __init__(self, size, percentages, empty_percent, n_traits=2, min_rate=0.3, max_rate=1, max_iter=10000):

		self.max_iter = max_iter
		self.square_size = 15
		self.square = pygame.Surface([self.square_size, self.square_size])
		self.empty_colour = (255, 255, 255)
		self.border = 1
		self.border_colour = (0, 0, 0)
		self.empty_colour = (255, 255, 255)
		self.text_colour = (0,51,102)
		self.text_font = pygame.font.SysFont("times new roman", 15, bold=True)
		self.n_traits = n_traits
		colours = [(168, 0, 0), (6, 52, 62), (30, 117, 41), (255, 128, 0), (141, 69, 155)]
		self.trait_colours = colours[:self.n_traits]

		self.rows = int(size[0])
		self.cols = int(size[1])
		self.city_grid = np.zeros((self.rows, self.cols))
		self.percentages = percentages
		self.empty_percent = empty_percent
		self.min_rate = min_rate
		self.max_rate = max_rate
		self.empty = []

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
			self.empty += [raw_index[rnd_index]]
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

		self.unhappy = []
		self.set_unhappy()
		self.info = dict()
		self.info["Initial Segregation Level: "] = round(self.segregation_level())
		self.info["Initial Isolation Level: "] = round(self.isolation_level())

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

		k = 0
		for i in self.info:
			pos = vec(950, 250 + k*30)
			if(i[0] != "U"):
				text_surface = self.text_font.render(i + str(self.info[i]) + "%", False, self.text_colour)
			else:
				text_surface = self.text_font.render(i + str(self.info[i]), False, self.text_colour)
			window.blit(text_surface, pos)
			k += 1

	def update(self):
		if len(self.unhappy) > 0 and self.update_iter < self.max_iter:
			rnd_index_empty = rnd.randint(0,len(self.empty)-1)
			index_empty_processed = self.gen_index(self.empty[rnd_index_empty])
			rnd_index_unhappy = rnd.randint(0,len(self.unhappy)-1)
			index_unhappy_processed = self.gen_index(self.unhappy[rnd_index_unhappy])
			value = self.city_grid[index_unhappy_processed[0], index_unhappy_processed[1]]

			self.empty += [self.unhappy[rnd_index_unhappy]]
			self.city_grid[index_unhappy_processed[0], index_unhappy_processed[1]] = 0
			self.city_grid[index_empty_processed[0], index_empty_processed[1]] = value
			self.empty.pop(rnd_index_empty)
			self.unhappy.pop(rnd_index_unhappy)

			self.update_unhappy(index_unhappy_processed, index_empty_processed)

			self.update_iter +=1
		else:
			if len(self.unhappy) == 0:
				self.info["Final Segregation Level: "] = round(self.segregation_level())
				self.info["Final Isolation Level: "] = round(self.isolation_level())
				self.info["Unhappy People: "] = len(self.unhappy)
			elif self.update_iter == self.max_iter:
				self.info["Final Segregation Level: "] = round(self.segregation_level())
				self.info["Final Isolation Level: "] = round(self.isolation_level())
				self.info["Unhappy People: "] = len(self.unhappy)
			self.running = False

	def gen_index(self, value):
		x = math.floor(value/self.cols)
		y = value%self.cols
		return [x, int(y)]

	def gen_raw_index(self, index):
		return int(index[0]*self.cols + index[1])
		
	def update_unhappy(self, pos, empty):
		for i in [-1,0,1]:
			for j in [-1,0,1]:

				if i != 0 and j != 0:
					raw_pos = self.gen_raw_index([pos[0]+i, pos[1]+j])
					if self.check_unhappy([pos[0]+i, pos[1]+j]):					
						if not raw_pos in self.unhappy:
							self.unhappy += [raw_pos]
					else:
						if raw_pos in self.unhappy:
							self.unhappy.remove(raw_pos)
				
				raw_empty = self.gen_raw_index([empty[0]+i, empty[1]+j])
				if self.check_unhappy([empty[0]+i, empty[1]+j]):				
					if not raw_empty in self.unhappy:
						self.unhappy += [raw_empty]
				else:
					if raw_empty in self.unhappy:
						self.unhappy.remove(raw_empty)

	def set_unhappy(self):
		for i in range(self.rows):
			for j in range(self.cols):
				if self.check_unhappy([i,j]):
					self.unhappy += [self.gen_raw_index([i,j])]


	def check_unhappy(self, position):
		x = position[0]
		y = position[1]

		if 0 <= x < self.rows and 0 <= y < self.cols:
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
					return True
			else:
				return False
		else:
			return False

	def check_segregated(self, position):
		x = position[0]
		y = position[1]

		if 0 <= x < self.rows and 0 <= y < self.cols:
			diff = 0
			pos = self.city_grid[x,y]

			if pos != 0:			
				for i in [-1,0,1]:
					for j in [-1,0,1]:
						if 0 <= x + i < self.rows and 0 <= y + j < self.cols and not (i == 0 and j == 0):
							neig = self.city_grid[x+i, y+j]
							if neig != 0 and pos != neig:
								diff += 1
				return diff == 0
			else:
				return False
		else:
			return False

	def neighbour_segregated(self, pos, grid):
		if grid[pos[0], pos[1]] == 0:
			return True
		else:
			for i in [-1, 0, 1]:
				for j in [-1, 0, 1]:
					x = pos[0] + i
					y = pos[1] + j
					if i != 0 and j != 0 and 0 <= x < self.rows and 0 <= y < self.cols:
						if self.city_grid[pos[0], pos[1]] == self.city_grid[x, y] and grid[x, y] == 0:
							return True
			return False

	def segregation_level(self):
		seg_grid = np.ones((self.rows, self.cols))
		for i in range(self.rows):
			for j in range(self.cols):
				if self.check_segregated([i,j]):
					seg_grid[i,j] = 0
		for i in range(self.rows):
			for j in range(self.cols):
				if self.neighbour_segregated([i,j], seg_grid):
					seg_grid[i,j] = 0
		return ((self.total_dim - np.count_nonzero(seg_grid))/self.total_dim)*100

	def isolation_level(self):
		isol = 0
		for i in range(self.rows):
			for j in range(self.cols):
				if self.check_segregated([i,j]):
					isol += 1
		return (isol/self.total_dim)*100