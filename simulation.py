import pygame
import sys
from text_box import text_box
import City

#ola sou a mariana e estou a expeirmentar o git
pygame.init()

#Creating window and setting size
win = pygame.display.set_mode((1200,650))#, pygame.FULLSCREEN)
#Name of the app
pygame.display.set_caption("Schelling Model Simulation")

text_boxes = []
text_boxes += [text_box(0, 1000, 100, 100, 20, border=2, is_number=True)]
text_boxes += [text_box(1, 1000, 150, 100, 20, border=2)]
text_boxes += [text_box(2, 1000, 200, 100, 20, border=2)]

box_inputs = ['' for _ in range(len(text_boxes))]

simulation_city = City.city([60,35])

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
			if event.key == 27:
				pygame.quit()
				sys.exit()
			elif event.key == 13:
				for box in text_boxes:
					if box.active:
						box_inputs[box.id] = box.return_value()
				print(box_inputs)
			else:
				for box in text_boxes:
					if box.active:
						box.add_text(event.key)

	#Update

	#Draw
	for box in text_boxes:
		box.draw(win)

	simulation_city.draw(win)


	pygame.display.update()
