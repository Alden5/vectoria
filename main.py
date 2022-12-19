import sys, pygame
window_size = (500,400)

pygame.init()

window = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

pygame.display.set_caption('Vectoria')


pixel_font = pygame.font.Font('Monocraft.otf',18)

line_surface = pygame.Surface(window_size)


def draw_text(text,position):
	text_surface = pixel_font.render(text, False, 'white')
	window.blit(text_surface,(position))

class Line:
	def __init__(self,p1,p2):
		self.p1 = p1
		self.p2 = p2

	
	def draw (self):
		pygame.draw.line(line_surface,'white',self.p1,self.p2,5)
		window.blit(line_surface,(0,0))

line1 = Line((100,100),(200,200))
while True:
	
	# Event handeler 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	
	
	
	line1.draw()
	draw_text('test',(5,5))
	
	
	
	
	# Update window
	pygame.display.update()
	
	
	# Limit fps to 60
	clock.tick(60)