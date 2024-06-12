import pdb
import sys
import re
EXAMPLE = 'example.txt'
INPUT = 'input.txt'
DIMENSIONS = 5

class Tile:
	def __init__(self, val: int):
		self.val = val
		self.visited = False

with open(INPUT) as f:
	draws = map(lambda el: int(el), f.readline().strip().split(','))
	tables = map(lambda el: list(map(lambda x: Tile(int(x)), re.split(' +', el.strip()))), filter(lambda el: el != '\n', f.readlines()))
	tables: list[tuple[list[list[Tile]], list[Tile], list[Tile], list[Tile], list[Tile]]] = list(zip(tables, tables, tables, tables, tables))

assert len(tables)[0] == DIMENSIONS
assert len(tables)[0][0] == DIMENSIONS

coords = [(row, col) for row in range(DIMENSIONS) for col in range(DIMENSIONS)]

def check_win(table, coord) -> int:
	# Check horiz
	if all(map(lambda el: el.visited, table[coord[0]])):
		print('Horiz win')
		return True

	# Check vertical
	if all(map(lambda el: el.visited, [table[row][coord[1]] for row in range(DIMENSIONS)])):
		print('Vert win')
		return True

	# # Check top-left bottom-right diag
	# if coord[0] == coord[1] and all(map(lambda el: el.visited, [table[dim][dim] for dim in range(DIMENSIONS)])):
	# 	print('Diag win')
	# 	return True

	# # Check top-right bottom-left diag
	# if coord[0] + coord[1] == DIMENSIONS - 1 and all(map(lambda el: el.visited, [table[dim][4-dim] for dim in range(DIMENSIONS)])):
	# 	print('Diag2 win')
	# 	return True
	return False
		
for draw in draws:
	for i, table in enumerate(tables):
		for coord in coords:
			tile = table[coord[0]][coord[1]]
			if tile.val == draw:
				tile.visited = True
				if check_win(table, coord):
					unmarked_sum = sum(map(lambda el: el.val, filter(lambda el: not el.visited, [tile for row in table for tile in row])))
					print(i)
					print(unmarked_sum, draw)
					print(unmarked_sum * draw)
					sys.exit()
				break
