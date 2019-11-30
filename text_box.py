import pygame
import math
from box import box
vec = pygame.math.Vector2

class text_box(box):

	def __init__(self, x, y, width, height, title="", bg_colour=(166,166,166), active_colour=(255,255,255), 
		text_size=12, text_colour=(0,51,102), border=0, border_colour=(0,0,0), is_int=False, is_float=False):
		
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.pos = vec(x, y)
		self.title_pos = vec(x, y - 20)
		self.size = vec(width, height)
		self.image = pygame.Surface([width, height])
		self.bg_colour = bg_colour
		self.active_colour = active_colour
		self.active = False
		self.text = ""
		self.text_size = text_size
		self.font = pygame.font.SysFont("arial", self.text_size)
		self.title_font = pygame.font.SysFont("times new roman", math.floor(self.text_size*1.2), bold=True)
		self.title = title
		self.text_colour = text_colour
		self.border = border
		self.border_colour = border_colour
		self._numbers = [48,49,50,51,52,53,54,55,56,57,256,257,258,259,260,261,262,263,264,265]
		self.is_int = is_int
		self.is_float = is_float

	def draw(self, window):
		if not self.active:
			if self.border == 0:
				self.image.fill(self.bg_colour)
			else:
				self.image.fill(self.border_colour)
				pygame.draw.rect(self.image, self.bg_colour, 
					(self.border, self.border, self.width-self.border*2, self.height-self.border*2))

			#Rendering text to image
			text = self.font.render(self.text, False, self.text_colour)
			text_height = text.get_height()
			self.image.blit(text, (self.border*2, (self.height - text_height)//2))
		else:
			if self.border == 0:
				self.image.fill(self.active_colour)
			else:
				self.image.fill(self.border_colour)
				pygame.draw.rect(self.image, self.active_colour, 
					(self.border, self.border, self.width-self.border*2, self.height-self.border*2))

			#Rendering text to image
			text = self.font.render(self.text, False, self.text_colour)
			text_height = text.get_height()
			text_width = text.get_width()
			if text_width < self.width - self.border*2:
				self.image.blit(text, (self.border*2, (self.height - text_height)//2))
			else:
				self.image.blit(text, ((self.border*2)+(self.width-text_width-self.border*3), (self.height - text_height)//2))

		window.blit(self.image, self.pos)

	def draw_title(self, window):
		text_surface = self.title_font.render(self.title, False, self.text_colour)
		window.blit(text_surface, self.title_pos)

	def add_text(self, key):
		try:
			if not (self.is_int or self.is_float):
				#Backspace
				if key == 8:
					text = list(self.text)
					text.pop()
					self.text = ''.join(text)
				#Space
				elif key == 8:
					text = list(self.text)
					text.append(' ')
					self.text = ''.join(text)
				#Adding Numbers
				elif key in self._numbers:
					text = list(self.text)
					if key < 100:
						text.append(str(key-48))
					else:
						text.append(str(key-256))
					self.text = ''.join(text)
				#Dot
				elif key == 46:
					text = list(self.text)
					text.append('.')
					self.text = ''.join(text)
				#Adding letters
				elif chr(key).isalpha():
					text = list(self.text)
					text.append(chr(key))
					self.text = ''.join(text)
			else:
				#Numbers
				if key in self._numbers:
					text = list(self.text)
					if key < 100:
						text.append(str(key-48))
					else:
						text.append(str(key-256))
					self.text = ''.join(text)
				#Dot
				elif key == 46:
					text = list(self.text)
					text.append('.')
					self.text = ''.join(text)
				#Backspace
				if key == 8:
					text = list(self.text)
					text.pop()
					self.text = ''.join(text)
		except:
			pass

	def return_value(self):
		if self.is_int:
			return int(self.text)
		elif self.is_float:
			return float(self.text)
		else:
			return self.text