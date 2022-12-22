import sys, pygame
from render import Render
from data import Points, Spline
from interpolate import Interpolate
from event import event_handler

pygame.init()

window_size = (450,250)
window = pygame.display.set_mode(window_size)

canvas_surface = pygame.Surface(window_size)
clock = pygame.time.Clock()
pixel_font = pygame.font.Font('Monocraft.otf',18)
pygame.display.set_caption('Vectoria')


render = Render(canvas_surface,pixel_font,window)
	

spline_test = Spline(
(50,150),	# P1
(200,-150),	# P2
(0,450),	# P3
(400,100)	# P4
)

interpolated_spline_points = Points(Interpolate(spline_test.fetch(), 100))

# Main logic
while True:
	
	# Event handeler 
	
	event_handler()
	canvas_surface.fill((50,50,100))
	render.line(interpolated_spline_points,5,'white')
	render.text('cubic bezier interpolator',(8,8))
#	render.text(str(pygame.mouse.get_pos()),(5,5))
	render.update()

	
	clock.tick(60)

	


		