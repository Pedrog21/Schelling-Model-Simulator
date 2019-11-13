import pygame
from screen import screen
from text_box import text_box
from button import button
from City import city
import sys
vec = pygame.math.Vector2

class running_screen(screen):

	def __init__(self, width, height, window, delay=500):

		self.width = width
		self.height = height
		self.window = window
		self.running = False
		self.delay = delay


	def set_inputs(self, size, percentages, empty_percent, n_traits=2, min_rate=0.3, max_rate=1):
		self.percentages = percentages
		self.empty_percent = empty_percent
		self.n_traits = n_traits
		self.min_rate = min_rate
		self.max_rate = max_rate
		self.city = city(size, percentages, empty_percent, n_traits, min_rate, max_rate)

	def run(self):
		pygame.time.delay(self.delay)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				#Close window when ESC key is pressed
				if event.key == 27:
					pygame.quit()
					sys.exit()
		self.city.draw(self.window)
		if self.city.running:
			self.city.update()