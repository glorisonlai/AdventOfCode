from itertools import chain
from itertools import tee

DAYS = 20
start = [1]
reset = 4
birth = 6

for _ in range(DAYS):
    start = chain.from_iterable(map(lambda x: [x-1] if x > 0 else [reset, birth], start))
    start, cpy = tee(start)
    print(_+1, list(cpy))

    
