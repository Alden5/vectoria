import pygame


def event_handler():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				pass
			if event.key == pygame.K_UP:
				definition += 1
			if event.key == pygame.K_DOWN:
				definition -= 1