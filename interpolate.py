from math import lerp

def Interpolate(points,definition):
	
	P1,P2,P3,P4 = points
	
	interpolated_points = []
	lerp_value = 0
	for x in range(definition+1):
		A = lerp(P1,P2,lerp_value)
		B = lerp(P2,P3,lerp_value)
		C = lerp(P3,P4,lerp_value)
		D = lerp(A,B,lerp_value)
		E = lerp(B,C,lerp_value)
		P = lerp(D,E,lerp_value)
		interpolated_points.append(P)
		lerp_value += 1/definition
	return interpolated_points
		
		

	

		