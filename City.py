import numpy as np

#Size is an array [a, b] where a is the width and b is the length of the city grid

class city:

	def __init__(self, size, n_traits):
		self.width = size(size[0])
		self.height = size(size[1])
		self.city_grid = np.zeros(self.width, self.height)
		self.image = pygame.Surface([width, height])

		
	def draw(self, initial_coordinates):
		x0 = initial_coordinates[0]
		y0 = initial_coordinates[1]

		for i in range(self.width):
			for j in range(self.height):
				self.image.fill(self.border_colour)
				pygame.draw.rect(self.image, self.active_colour, 
					(self.border, self.border, self.width-self.border*2, self.height-self.border*2))
