import re
import itertools
import functools

INPUT_FILE = 'input.txt'

hori_v = 0
vert_v = 0

with open(INPUT_FILE, 'r') as f:
	for line in f:
		magnitude = int(re.search(r'\d+', line).group())
		dir = re.search(r'[a-z]+', line).group()
		match dir:
			case 'up':
				vert_v -= magnitude
			case 'down':
				vert_v += magnitude
			case 'forward':
				hori_v += magnitude

print(hori_v * vert_v)