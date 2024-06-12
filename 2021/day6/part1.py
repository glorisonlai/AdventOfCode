from itertools import chain 

input = 'input.txt'
example = 'example.txt'

with open(input, 'r') as in_file:
    fish = map(lambda x: int(x), in_file.readline().strip().split(','))

DAYS = 256 

for _ in range(DAYS):
    fish = chain.from_iterable(map(lambda x: [x-1] if x > 0 else [6, 8], fish))

print(len(list(fish)))
