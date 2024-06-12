class Coord:
    def __init__(self, x: str, y: str):
        self.x = int(x)
        self.y = int(y)

with open('example.txt', 'r') as in_file:
    coord_pairs = map(lambda line: tuple(map(lambda pair: Coord(*pair.split(',')), line.strip().split(' -> '))), in_file.readlines())

coord_pairs_1d = filter(lambda pair: pair[0].x == pair[1].x or pair[0].y == pair[1].y, coord_pairs)

seen_coords = {}
for pair in coord_pairs_1d:
    larger_x, smaller_x = max(pair[0].x, pair[1].x), min(pair[0].x, pair[1].x)
    larger_y, smaller_y = max(pair[0].y, pair[1].y), min(pair[0].y, pair[1].y)

    for x in range(smaller_x, larger_x+1):
        for y in range(smaller_y, larger_y+1):
            seen_coords.setdefault((x,y), 0)
            seen_coords[(x,y)] += 1

print(len(list(filter(lambda e: e > 1, seen_coords.values()))))

