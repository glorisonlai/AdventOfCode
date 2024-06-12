import math

INPUT = 'input.txt'
EXAMPLE = 'example.txt'

with open(EXAMPLE, 'r') as in_file:
    positions = list(map(lambda x: int(x), in_file.readline().strip().split(',')))



