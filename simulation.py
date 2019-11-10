import pygame
import sys
from text_box import text_box
import box
from button import button
import City

#ola sou a mariana e estou a expeirmentar o git e sou ganda croma
pygame.init()

#Creating window and setting size
win = pygame.display.set_mode((1200,650))#, pygame.FULLSCREEN)
#Name of the app
pygame.display.set_caption("Schelling Model Simulation")

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
buttons = []
#buttons += button()

#Max 65x41 for now
simulation_city = City.city([1,1])

run = True
while run:
	#Changing background colour of the screen
	win.fill((243,193,74))

	#Events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			for box in text_boxes:
				box.check_click(pygame.mouse.get_pos())
		if event.type == pygame.KEYDOWN:
			#Close window when ESC key is pressed
			if event.key == 27:
				pygame.quit()
				sys.exit()
			#Write text in active boxes
			else:
				for box in text_boxes:
					if box.active:
						box.add_text(event.key)

	#Update

	#Draw
	for box in text_boxes:
		box.draw(win)
		box.draw_title(win)

	simulation_city.draw(win)


	pygame.display.update()
