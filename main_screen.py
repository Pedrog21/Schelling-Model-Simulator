import pygame
from screen import screen
from text_box import text_box
from button import button
import sys
vec = pygame.math.Vector2

class main_screen(screen):

	def __init__(self, width, height, window, screen_type):

		self.width = width
		self.height = height
		self.window = window

		self.running = True
		self.traits_ready = False
		self.text_boxes = []
		self.buttons = []
		self.buttons_dic = dict()
		self.screen_type = screen_type
		self.extra_boxes = 0

		if(self.screen_type == "Regular Model"):
			#Adding Text Boxes
			self.text_boxes += [text_box(1000, 150, 100, 20, title="Empty Spots (%)", border=1, is_float=True)]
			self.text_boxes += [text_box(1000, 200, 100, 20, title="Width", border=1, is_int=True)]
			self.text_boxes += [text_box(1000, 250, 100, 20, title="Height", border=1, is_int=True)]
			self.buttons += [button(1000, 100, 45, 20, text="2 Traits", text_size=10, hor_space=15, ver_space=4)]
			self.buttons_dic["2 Traits"] = False
			self.buttons += [button(1050, 100, 45, 20, text="3 Traits", text_size=10, hor_space=15, ver_space=4)]
			self.buttons_dic["3 Traits"] = False

		self.box_inputs = dict()

		#Adding Buttons
		self.start_button = button(1000, 450, 100, 40, text="Run", hor_space=50, ver_space=3)

		self.intro_font = pygame.font.SysFont("times new roman", 40, bold=True)
		self.intro_text_colour = (0,51,102)
		self.intro_message = "Set the parameters"
		self.intro_pos = vec(self.width//10, self.height//5)

	def run(self):
		#Showing intro message
		text_surface = self.intro_font.render(self.intro_message, False, self.intro_text_colour)
		self.window.blit(text_surface, self.intro_pos)

		#Update number of extra boxes
		self.add_boxes()

		#Events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			#Check where the mouse clicks
			if event.type == pygame.MOUSEBUTTONDOWN:
				for box in self.text_boxes:
					box.check_click(pygame.mouse.get_pos())
				for button in self.buttons:
					button.check_click(pygame.mouse.get_pos())
					if button.active:
						self.buttons_dic[button.text] = True	
						if button.text == "2 Traits":
							self.buttons_dic["3 Traits"] = False
							self.extra_boxes = 2
						else:
							self.extra_boxes = 3
							self.buttons_dic["2 Traits"] = False
					if not self.buttons_dic[button.text]:
						button.deactivate()
				self.start_button.check_click(pygame.mouse.get_pos())
				if self.start_button.active:
					if self.inputs_ready():
						self.running = False
						for box in self.text_boxes:	
							self.box_inputs[box.title] = box.return_value()
					else:
						self.start_button.active = False					
			if event.type == pygame.KEYDOWN:
				#Close window when ESC key is pressed
				if event.key == 27:
					pygame.quit()
					sys.exit()
				#Configuring TAB key to change to the next text box
				elif event.key == 9:
					for i in range(len(self.text_boxes)):
						if self.text_boxes[i].active:
							self.text_boxes[i].active = False
							if i == len(self.text_boxes)-1:
								self.text_boxes[0].active = True
								break
							else:
								self.text_boxes[i+1].active = True
								break
				else:	
					#Write text in active boxes
					for box in self.text_boxes:
						if box.active:
							box.add_text(event.key)

		#Drawing boxes and buttons			
		for box in self.text_boxes:
			box.draw(self.window)
			box.draw_title(self.window)
		self.start_button.draw(self.window)
		for button in self.buttons:
			button.draw(self.window)

	def inputs_ready(self):
		try:
			return (0 <= self.box_inputs["Number of Traits"] <= 1 and 0 <= self.box_inputs["Empty Spots (%)"] <= 1 
				and self.box_inputs["Width"] != "" and self.box_inputs["Height"] != "")
		except:
			return False
	
	def inputs(self):
		return [[self.box_inputs["Width"], self.box_inputs["Height"]], 
			[self.box_inputs["Red/Blue (%)"], 1 - self.box_inputs["Red/Blue (%)"]],
			self.box_inputs["Empty Spots (%)"]]

	def add_boxes(self):
		k = len(self.text_boxes) - 3
		while k != self.extra_boxes:
			if self.extra_boxes > k:
				self.text_boxes += [text_box(1000, 300 + k*50, 100, 20, title="Percentage " + str(k+1), border=1, is_float=True)]
			else:
				self.text_boxes.pop()
			k = len(self.text_boxes) - 3
		return


