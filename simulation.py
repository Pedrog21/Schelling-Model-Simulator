import pygame
import sys
from text_box import text_box
import box
from button import button
import City
vec = pygame.math.Vector2

pygame.init()

#Creating window and setting size
height = 650
width = 1200
win = pygame.display.set_mode((width,height))#, pygame.FULLSCREEN)
#Name of the app
pygame.display.set_caption("Schelling Model's Simulation")

#Max 65x41 for now
simulation_city = City.city()

#Intro Settings
is_beggining = True
end_beginning = False


run = True
while run:
	#Changing background colour of the screen
	win.fill((243,193,74))

	#Intro Message
	if is_beggining:
		text_surface = intro_font.render(intro_message, False, intro_text_colour)
		win.blit(text_surface, intro_pos)
		#Para apagar!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		text_surface = intro_font_1.render("Version 1.0", False, intro_text_colour)
		win.blit(text_surface, intro_pos_1)

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
				end_beginning = True
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
	if not end_beginning:
		is_beginning = False
	if simulation_city.running and start_button.active:
		simulation_city.run(box_inputs)

	#Draw
	for box in text_boxes:
		box.draw(win)
		box.draw_title(win)
	start_button.draw(win)
	if simulation_city.running:
		simulation_city.draw(win)

	#Update
	pygame.display.update()
