import math

def height_reached(t: int, start_y: int):
	print(f'{t}: {t*start_y - t**2/2 + t/2}')

def max_height(start_y: int):
	max_t = (2*start_y + 1) / 2
	height_reached(math.floor(max_t), start_y)

def target(t: int):
	for y in range(-90, -56):
		print(y/t + t/2 - 1/2)

