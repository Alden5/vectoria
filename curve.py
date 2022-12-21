from math import *
from decimal import Decimal
# Cubic bezier interpolator

orgin = (100,200)
orgin_handle = (200,100)
destination_handle = (200,300)
destination = (300,200)


spline_points = []
definition = 100
lerp_value = 0


for x in range(definition+1):
	A = lerp(orgin,orgin_handle,lerp_value)
	B = lerp(orgin_handle,destination_handle,lerp_value)
	C = lerp(destination_handle,destination,lerp_value)
	D = lerp(A,B,lerp_value)
	E = lerp(B,C,lerp_value)
	P = lerp(D,E,lerp_value)
	
	print(P)
	lerp_value += 1/definition



