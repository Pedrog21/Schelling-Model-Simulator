import pygame
from screen import screen
from text_box import text_box
from button import button
from city import city
import sys
vec = pygame.math.Vector2

class running_screen(screen):

	def __init__(self, width, height, window, screen_type, delay=0):

		self.width = width
		self.height = height
		self.window = window
		self.running = True
		self.delay = delay
		self.screen_type = screen_type
		self.back_button = button(1000, 400, 100, 40, text="Back", hor_space=40, ver_space=2)


	def set_inputs(self, size, percentages, empty_percent, n_traits=2, min_rate=0.3, max_rate=1):
		self.percentages = percentages
		self.empty_percent = empty_percent
		self.n_traits = n_traits
		self.min_rate = min_rate
		self.max_rate = max_rate
		self.city = city(size, percentages, empty_percent, n_traits, min_rate, max_rate)

	def run(self):
		#Checking if back button is active to stop running
		if self.back_button.active:
			self.running = False

		#Checking for events
		pygame.time.delay(self.delay)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				self.back_button.check_click(pygame.mouse.get_pos())
			if event.type == pygame.KEYDOWN:
				#Close window when ESC key is pressed
				if event.key == 27:
					pygame.quit()
					sys.exit()

		#Create back button
		if not self.city.running:
			self.back_button.draw(self.window)

		#Draw city grid
		self.city.draw(self.window)
		
		#Update
		if self.city.running:
			self.city.update()
		else:
			pass