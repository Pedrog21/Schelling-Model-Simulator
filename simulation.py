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
first = first_screen(width, height, win)

#Info about current screen
screens = dict()
screens["first"] = True

run = True
while run:
	#Changing background colour of the screen
	win.fill((131,131,131))

	#Selection of screen to show
	if screens["first"]:
		first.run()
		screens["first"] = first.running
		if not screens["first"]:
			screens["main"] = True
			if first.action() == "Neighbourhoods":
				main = main_screen1(width, height, win)
			else:
				main = main_screen(width, height, win)
	elif screens["main"]:
		inps = main.run()
		screens["main"] = main.running
		if not screens["main"]:
			inps = main.return_inputs()
			screens["running"] = True
			running = running_screen(width, height, win, "city")
			running.set_inputs(inps["size"], inps["percent"], inps["empty"], inps["traits"], inps["min"], inps["max"])
	else:
		running.run()
		screens["running"] = running.running
		if not screens["running"]:
			screens["first"] = True
			first = first_screen(width, height, win)

	#Update
	pygame.display.update()
