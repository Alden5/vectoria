# Line data class
class Points:
	def __init__(self,points):
		self.points = points
		
	def fetch(self):
		return self.points
	
class Spline:
	def __init__(self,P1,P2,P3,P4):
		self.P1 = P1
		self.P2 = P2
		self.P3 = P3
		self.P4 = P4
	
	def fetch(self):
		return (self.P1,self.P2,self.P3,self.P4)