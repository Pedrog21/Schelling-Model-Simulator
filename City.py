import numpy as np

#Size is an array [a, b] where a is the width and b is the length of the city grid

class City:
	
	def __init__(self, size):
		self.city_grid = np.zeros((size[0], size[1]))