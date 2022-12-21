
def lerp(a, b, t):
	ax, ay = a
	bx, by = b
	return ((1 - t) * ax + t * bx),((1 - t) * ay + t * by)
