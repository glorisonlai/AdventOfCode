import pdb
import itertools
import functools
INPUT_FILE = 'input1.txt'

with open(INPUT_FILE, 'r') as in_file:
	lines = in_file.readlines()

nums = map(lambda s: int(s.strip()), lines)
group1, group2 = itertools.tee(nums)
filtered = filter(lambda args: args[1] > args[0], zip(group1, itertools.islice(group2, 1, None)))
agg = functools.reduce(lambda sum, _: sum + 1, filtered, 0)
print(agg)