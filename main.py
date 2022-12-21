import sys, pygame
from classes import *

pygame.init()

window_size = (500,400)
window = pygame.display.set_mode(window_size)
canvas_surface = pygame.Surface(window_size)
clock = pygame.time.Clock()
pixel_font = pygame.font.Font('Monocraft.otf',18)
pygame.display.set_caption('Vectoria')


renderer = Render(canvas_surface,pixel_font,window,60,clock)
		
line1 = Points(((100,100),(200,200),(300,100)))


# Main logic
while True:
	
	# Event handeler 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				pass

	
	renderer.lines(line1)
	renderer.text('test',(5,5))
	renderer.update()

	


		