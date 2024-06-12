import pdb
from itertools import pairwise
import re

INPUT = 'input.txt'
EXAMPLE = 'example.txt'


def main():
    with open(INPUT, 'r') as in_file:
        start = in_file.readline().strip()
        in_file.readline()
        recipe_pattern = re.compile(r'([a-z]*) -> ([a-z]*)', re.I)
        recipes = {match.group(1): match.group(2) for match in map(lambda line: re.match(recipe_pattern, line.strip()), in_file.readlines())}

    for _ in range(10):
        keys = [pair for pair in pairwise(start)]
        insert = map(lambda pair: recipes[''.join(pair)],keys)
        start = [letter for sublist in zip([char for char in start], insert) for letter in sublist]+[start[-1]]

    counter = {}
    for letter in start:
        counter.setdefault(letter, 0)
        counter[letter] += 1

    print(counter[max(counter, key=counter.get)] - counter[min(counter, key=counter.get)])
main()
