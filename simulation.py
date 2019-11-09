import pygame

pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Schelling Model Simulation")

run = True
while run:
	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.draw.circle(win, (0, 0, 255), (250, 250), 20)
	pygame.display.update()

pygame.quit()