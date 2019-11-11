import pygame
import sys
from text_box import text_box
from button import button
from main_screen import main_screen
from running_screen import running_screen
import box
import City
vec = pygame.math.Vector2

pygame.init()

#Creating window and setting size
height = 650
width = 1200
win = pygame.display.set_mode((width,height))#, pygame.FULLSCREEN)
#Name of the app
pygame.display.set_caption("Schelling Model's Simulation")

#Creating main screen
is_beginning = True
main_screen = main_screen(width, height, win)

#Creating empty running screen
running_screen = running_screen(width, height, win)
inputs_do = True

run = True
while run:
	#Changing background colour of the screen
	win.fill((243,193,74))

	if is_beginning:
		main_screen.run()
		is_beginning = main_screen.running
	if not is_beginning:
		if inputs_do:
			running_inputs = main_screen.inputs()
			running_screen.set_inputs(running_inputs[0], running_inputs[1], running_inputs[2])
			inputs_do = False
		running_screen.run()

	#Update
	pygame.display.update()
