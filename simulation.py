import pygame
import sys
from text_box import text_box
from button import button
from main_screen import main_screen
from running_screen import running_screen
from first_screen import first_screen
import box
import city
vec = pygame.math.Vector2

pygame.init()

#Creating window and setting size
height = 650
width = 1200
win = pygame.display.set_mode((width,height))#, pygame.FULLSCREEN)
#Name of the app
pygame.display.set_caption("Schelling Model's Simulation")

#Creating first screen
first_screen = first_screen(width, height, win)

#Info about current screen
screens = dict()
screens["first"] = True

run = True
while run:
	#Changing background colour of the screen
	win.fill((131,131,131))

	#Selection of screen to show
	if screens["first"]:
		first_screen.run()
		screens["first"] = first_screen.running
		if not screens["first"]:
			screens["main"] = True
			main_screen = main_screen(width, height, win, first_screen.action())
	elif screens["main"]:
		main_screen.run()
		screens["main"] = main_screen.running
		if not screens["main"]:
			inputs = main_screen.inputs()
			screens["running"] = True
			running_screen = running_screen(width, height, win, "city")
			running_screen.set_inputs()
	else:
		running_screen.run()
		screens["running"] = running_screen.running
		if not screens["running"]:
			screens["first"] = True
			first_screen = first_screen(width, height, win)

	#Update
	pygame.display.update()
