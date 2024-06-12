from math import factorial
from math import ceil 
import pdb

input = 'input.txt'
example = 'example.txt'
ex = 'ex.txt'

with open(ex, 'r') as in_file:
    fishes = list(map(lambda x: int(x), in_file.readline().strip().split(',')))

DAYS = 8

total_fish = len(fishes)
for fish in fishes:
    if DAYS < fish: continue
    birthing_rounds = (DAYS - fish) // 8 + 1

    increase = ceil((birthing_rounds*((DAYS-fish)-8*(factorial(birthing_rounds - 1) if birthing_rounds > 1 else 0))) / 6)
    start = DAYS - fish
    iterations = -8 * (factorial(birthing_rounds -  1) if birthing_rounds > 1 else 0)
    total_fish += increase
    print(birthing_rounds, increase, total_fish)
    print(start, iterations)
    #pdb.set_trace()

#print(birthing_rounds, increase, total_fish)

