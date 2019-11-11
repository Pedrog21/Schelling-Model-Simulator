import pygame
from screen import screen
from text_box import text_box
from button import button

class main_screen(screen):

	def __init__(self):

		#Adding Text Boxes
		self.text_boxes = []
		self.text_boxes += [text_box(1000, 100, 100, 20, title="Number of Traits", border=1, is_number=True)]
		self.text_boxes += [text_box(1000, 150, 100, 20, title="Similar (%)", border=1, is_number=True)]
		self.text_boxes += [text_box(1000, 200, 100, 20, title="Red/Blue (%)", border=1, is_number=True)]
		self.text_boxes += [text_box(1000, 250, 100, 20, title="Empty Spots (%)", border=1, is_number=True)]
		self.text_boxes += [text_box(1000, 300, 100, 20, title="Width", border=1, is_number=True)]
		self.text_boxes += [text_box(1000, 350, 100, 20, title="Height", border=1, is_number=True)]

		self.box_inputs = {}

		#Adding Buttons
		self.start_button = button(1000, 400, 100, 40, text="Run")

		self.intro_font = pygame.font.SysFont("times new roman", 40, bold=True)
		self.intro_font_1 = pygame.font.SysFont("times new roman", 20, bold=True)
		self.intro_text_colour = (0,51,102)
		self.intro_message = "Welcome to Schelling Model's Simulation!"
		self.intro_pos = vec(width//10, height//5)
		self.intro_pos_1 = vec(width//1.8, height//3)