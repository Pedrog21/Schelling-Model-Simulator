import pygame
from screen import screen
from text_box import text_box
from button import button
import sys
vec = pygame.math.Vector2

class main_screen(screen):

	def __init__(self, width, height, window):

		self.width = width
		self.height = height
		self.window = window

		self.running = True

		#Adding Text Boxes
		self.text_boxes = []
		self.text_boxes += [text_box(1000, 100, 100, 20, title="Number of Traits", border=1, is_int=True)]
		self.text_boxes += [text_box(1000, 150, 100, 20, title="Similar (%)", border=1, is_float=True)]
		self.text_boxes += [text_box(1000, 200, 100, 20, title="Red/Blue (%)", border=1, is_float=True)]
		self.text_boxes += [text_box(1000, 250, 100, 20, title="Empty Spots (%)", border=1, is_float=True)]
		self.text_boxes += [text_box(1000, 300, 100, 20, title="Width", border=1, is_int=True)]
		self.text_boxes += [text_box(1000, 350, 100, 20, title="Height", border=1, is_int=True)]

		self.box_inputs = {}

		#Adding Buttons
		self.start_button = button(1000, 400, 100, 40, text="Run")

		self.intro_font = pygame.font.SysFont("times new roman", 40, bold=True)
		self.intro_font_1 = pygame.font.SysFont("times new roman", 20, bold=True)
		self.intro_text_colour = (0,51,102)
		self.intro_message = "Welcome to Schelling Model's Simulation!"
		self.intro_pos = vec(self.width//10, self.height//5)
		self.intro_pos_1 = vec(self.width//1.8, self.height//3)

	def run(self):
		#Showing intro message
		text_surface = self.intro_font.render(self.intro_message, False, self.intro_text_colour)
		self.window.blit(text_surface, self.intro_pos)
		#Para apagar!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		text_surface = self.intro_font_1.render("Version 1.0", False, self.intro_text_colour)
		self.window.blit(text_surface, self.intro_pos_1)

		#Events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			#Check where the mouse clicks
			if event.type == pygame.MOUSEBUTTONDOWN:
				for box in self.text_boxes:
					box.check_click(pygame.mouse.get_pos())
				self.start_button.check_click(pygame.mouse.get_pos())
				if self.start_button.active:
					for box in self.text_boxes:	
						self.box_inputs[box.title] = box.return_value()
			if event.type == pygame.KEYDOWN:
				#Close window when ESC key is pressed
				if event.key == 27:
					pygame.quit()
					sys.exit()
				else:
					#Write text in active boxes
					for box in self.text_boxes:
						if box.active:
							box.add_text(event.key)

		#Drawing boxes					
		for box in self.text_boxes:
			box.draw(self.window)
			box.draw_title(self.window)
		self.start_button.draw(self.window)

		if self.inputs_ready():
			self.running = False

	def inputs_ready(self):
		try:
			return (0 <= self.box_inputs["Red/Blue (%)"] <= 1 and 0 <= self.box_inputs["Empty Spots (%)"] <= 1 
				and self.box_inputs["Width"] != "" and self.box_inputs["Height"] != "")
		except:
			return False
	
	def inputs(self):
		return [[self.box_inputs["Width"], self.box_inputs["Height"]], 
			[self.box_inputs["Red/Blue (%)"], 1 - self.box_inputs["Red/Blue (%)"]],
			self.box_inputs["Empty Spots (%)"]]