import pygame
vec = pygame.math.Vector2

class text_box():

	def __init__(self, x, y, width, height, bg_colour=(166,166,166), active_colour=(255,255,255), 
		text_size=12, text_colour=(0,0,0), border=0, border_colour=(0,0,0), is_number=False):
		
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.pos = vec(x, y)
		self.size = vec(width, height)
		self.image = pygame.Surface([width, height])
		self.bg_colour = bg_colour
		self.active_colour = active_colour
		self.active = False
		self.text = ""
		self.text_size = text_size
		self.font = pygame.font.SysFont("arial", self.text_size)
		self.text_colour = text_colour
		self.border = border
		self.border_colour = border_colour
		self._numbers = [48,49,50,51,52,53,54,55,56,57]
		#self._special = [8,13,32]
		self.is_number = is_number

	def update(self):
		pass

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

	def add_text(self, key):
		try:
			if not self.is_number:
				#Adding letters
				if chr(key).isalpha():
					text = list(self.text)
					text.append(chr(key))
					self.text = ''.join(text)
					print(self.text)
				#Backspace
				elif key == 8:
					text = list(self.text)
					text.pop()
					self.text = ''.join(text)
				#Space
				elif key == 8:
					text = list(self.text)
					text.append(' ')
					self.text = ''.join(text)
				#Numbers
				elif key in self._numbers:
					text = list(self.text)
					text.append(str(key-48))
					self.text = ''.join(text)
				#Dot
				elif key == 46:
					text = list(self.text)
					text.append('.')
					self.text = ''.join(text)
				else:
					print(key)
			else:
				#Numbers
				if key in self._numbers:
					text = list(self.text)
					text.append(str(key-48))
					self.text = ''.join(text)
				#Dot
				elif key == 46:
					text = list(self.text)
					text.append('.')
					self.text = ''.join(text)
				else:
					print(key)
		except:
			print(key)

	def check_click(self, pos):
		if pos[0] > self.x and pos[0] < self.x + self.width:
			if pos[1] > self.y and pos[1] < self.y + self.height:
				self.active = True
			else:
				self.active = False
		else:
			self.active = False

	def return_value(self):
		if not is_number:
			return self.text
		else:
			return self.float(text)