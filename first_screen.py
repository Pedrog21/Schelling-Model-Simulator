import pygame
from screen import screen
from text_box import text_box
from button import button
import sys
vec = pygame.math.Vector2

class first_screen(screen):

	def __init__(self, width, height, window):

		self.width = width
		self.height = height
		self.window = window

		self.running = True

		#Adding Buttons
		self.buttons = []
		self.buttons += [button(800, 400, 250, 40, text="Regular Model", hor_space=75, ver_space=2)]
		self.buttons += [button(150, 400, 250, 40, text="Neighbourhoods", hor_space=50, ver_space=2)]


		self.intro_font = pygame.font.SysFont("times new roman", 40, bold=True)
		self.intro_text_colour = (0,51,102)
		self.intro_message = "Welcome to Schelling Model's Simulation!"
		self.intro_pos = vec((self.width-len(self.intro_message)*18)/2, self.height//5)

	def run(self):
		#Showing intro message
		text_surface = self.intro_font.render(self.intro_message, False, self.intro_text_colour)
		self.window.blit(text_surface, self.intro_pos)

		#Events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			#Check where the mouse clicks
			if event.type == pygame.MOUSEBUTTONDOWN:
				for button in self.buttons:
					button.check_click(pygame.mouse.get_pos())
					if button.active:
						self.running = False
			if event.type == pygame.KEYDOWN:
				#Close window when ESC key is pressed
				if event.key == 27:
					pygame.quit()
					sys.exit()

		#Drawing boxes					
		for button in self.buttons:
			button.draw(self.window)
	
	def action(self):
		for button in self.buttons:
			if button.active:
				return button.text
		return 0