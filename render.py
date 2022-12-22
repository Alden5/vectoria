# Render functions class
import pygame
class Render:
	
	def __init__(self,line_surface,font,window):
		self.line_surface = line_surface
		self.window = window
		self.font = font

		
	def text(self,text,position):
		text_surface = self.font.render(text, False, 'white')
		self.window.blit(text_surface,(position))
	
	def line(self,points,width,color):
		for x in range(len(points.fetch())-1):
			pygame.draw.line(self.line_surface,color,points.fetch()[x],points.fetch()[x+1],width)
		self.window.blit(self.line_surface,(0,0))
		
	def dots(self,points,width,color):
		for x in range(len(points.fetch())):
			pygame.draw.circle(self.line_surface,color,points.fetch()[x],width)
		self.window.blit(self.line_surface,(0,0))
		
	def update(self):
		pygame.display.update()
		