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
	
	def lines(self,points):
		for x in range(len(points.fetch_points())-1):
			pygame.draw.line(self.line_surface,'white',points.fetch_points()[x],points.fetch_points()[x+1],5)
		self.window.blit(self.line_surface,(0,0))
		
	def dots(self,points):
		for x in range(len(points.fetch_points())):
			pygame.draw.circle(self.line_surface,'white',points.fetch_points()[x],2)
		self.window.blit(self.line_surface,(0,0))
		
		
	def update(self):
		pygame.display.update()
		