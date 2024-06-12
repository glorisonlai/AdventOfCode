#!/c/Users/Glorison Lai/AppData/Local/Programs/Python/Python310/python
import re

INPUT_FILE = 'input.txt'

hori_v = 0
vert_v = 0
aim = 0

with open(INPUT_FILE, 'r') as f:
	for line in f:
		magnitude = int(re.search(r'\d+', line).group())
		dir = re.search(r'[a-z]+', line).group()
		match dir:
			case 'up':
				aim -= magnitude
			case 'down':
				aim += magnitude
			case 'forward':
				hori_v += magnitude
				vert_v += aim * magnitude

print(hori_v * vert_v)