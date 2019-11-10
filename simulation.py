import pygame
import sys
from text_box import text_box
import box
from button import button
import City
vec = pygame.math.Vector2

#ola sou a mariana e estou a expeirmentar o git e sou ganda croma
pygame.init()

#Creating window and setting size
height = 650
width = 1200
win = pygame.display.set_mode((width,height))#, pygame.FULLSCREEN)
#Name of the app
pygame.display.set_caption("Schelling Model's Simulation")

#Adding Text Boxes
text_boxes = []
text_boxes += [text_box(1000, 100, 100, 20, title="Number of Traits", border=1, is_number=True)]
text_boxes += [text_box(1000, 150, 100, 20, title="Similar (%)", border=1, is_number=True)]
text_boxes += [text_box(1000, 200, 100, 20, title="Red/Blue (%)", border=1, is_number=True)]
text_boxes += [text_box(1000, 250, 100, 20, title="Empty Spots (%)", border=1, is_number=True)]
text_boxes += [text_box(1000, 300, 100, 20, title="Width", border=1, is_number=True)]
text_boxes += [text_box(1000, 350, 100, 20, title="Height", border=1, is_number=True)]

box_inputs = {}

#Adding Buttons
start_button = button(1000, 400, 100, 40, text="Run")

#Max 65x41 for now
simulation_city = City.city()

#Intro Settings
is_beggining = True
intro_font = pygame.font.SysFont("times new roman", 40, bold=True)
intro_text_colour = (0,51,102)
intro_message = "Welcome to Schelling Model's Simulation!"
intro_pos = vec(width//10, height//5)

run = True
while run:
	#Changing background colour of the screen
	win.fill((243,193,74))

	#Intro Message
	if is_beggining:
		text_surface = intro_font.render(intro_message, False, intro_text_colour)
		win.blit(text_surface, intro_pos)

	#Deactivating buttons
	if start_button.active:
		start_button.deactivate()

	#Events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		#Check where the mouse clicks
		if event.type == pygame.MOUSEBUTTONDOWN:
			for box in text_boxes:
				box.check_click(pygame.mouse.get_pos())
			start_button.check_click(pygame.mouse.get_pos())
			if start_button.active:
				for box in text_boxes:	
					box_inputs[box.title] = box.return_value()
				print(box_inputs)
		if event.type == pygame.KEYDOWN:
			#Close window when ESC key is pressed
			if event.key == 27:
				pygame.quit()
				sys.exit()
			else:
				#Write text in active boxes
				for box in text_boxes:
					if box.active:
						box.add_text(event.key)


	#Update
	if False:
		is_beggining = False

	#Draw
	for box in text_boxes:
		box.draw(win)
		box.draw_title(win)
	start_button.draw(win)
	if simulation_city.running:
		simulation_city.draw(win)

	#Update
	pygame.display.update()
