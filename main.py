import sys, pygame
from render import *
from data import *
from curve import *
from math import *

pygame.init()

window_size = (450,250)
window = pygame.display.set_mode(window_size)




pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 5);
canvas_surface = pygame.Surface(window_size)
clock = pygame.time.Clock()
pixel_font = pygame.font.Font('Monocraft.otf',18)
pygame.display.set_caption('Vectoria')


renderer = Render(canvas_surface,pixel_font,window)
	



#
#Cubic bezier interpolator
p1 = (50,150)
p2 = (200,-150)
p3 = (0,450)
p4 = (400,100)


spline_points = []
definition = 10000
lerp_value = 0
for x in range(definition+1):
	A = lerp(p1,p2,lerp_value)
	B = lerp(p2,p3,lerp_value)
	C = lerp(p3,p4,lerp_value)
	D = lerp(A,B,lerp_value)
	E = lerp(B,C,lerp_value)
	P = lerp(D,E,lerp_value)
	spline_points.append(P)
	lerp_value += 1/definition
	
lerpy = Points(spline_points)





lerpy = Points(spline_points)

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
			if event.key == pygame.K_UP:
				definition += 1
			if event.key == pygame.K_DOWN:
				definition -= 1
	

	canvas_surface.fill((50,50,100))
	renderer.lines(lerpy)
	renderer.text('cubic bezier interpolator',(8,8))
#	renderer.text(str(pygame.mouse.get_pos()),(5,5))
	renderer.update()
	
	print(lerpy)
	
	clock.tick(60)

	


		