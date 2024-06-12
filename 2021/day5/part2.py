from itertools import repeat

class Coord:
    def __init__(self, x: str, y: str):
        self.x = int(x)
        self.y = int(y)


with open('input.txt', 'r') as in_file:
    coord_pairs = map(lambda line: tuple(map(lambda pair: Coord(*pair.split(',')), line.strip().split(' -> '))), in_file.readlines())

seen_coords = {}
for pair1, pair2 in coord_pairs:
    x_range = range(pair1.x, pair2.x + 1 if pair2.x >= pair1.x else pair2.x - 1, 1 if pair2.x >= pair1.x else -1)
    y_range = range(pair1.y, pair2.y + 1 if pair2.y >= pair1.y else pair2.y - 1, 1 if pair2.y >= pair1.y else -1)

    if pair1.x == pair2.x:
        x_range = repeat(pair1.x)
    elif pair1.y == pair2.y:
        y_range = repeat(pair1.y)
        
    for x,y in zip(x_range, y_range):
        seen_coords.setdefault((x,y), 0)
        seen_coords[(x,y)] += 1

print(len(list(filter(lambda e: e > 1, seen_coords.values()))))

