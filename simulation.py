import pygame

pygame.init()

#Creating window and setting size
win = pygame.display.set_mode((500,500))
#Name of the app
pygame.display.set_caption("Schelling Model Simulation")

run = True
while run:
	pygame.time.delay(100)

	#Check if exit button was pressed to exit the window
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	if run:
		pygame.draw.circle(win, (0, 0, 255), (250, 250), 20)
		pygame.display.update()

pygame.quit()