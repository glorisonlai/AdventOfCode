import pdb
import itertools
import functools
INPUT_FILE = 'input1.txt'

with open(INPUT_FILE, 'r') as in_file:
	lines = in_file.readlines()

nums = map(lambda s: int(s.strip()), lines)
group1, group2 = itertools.tee(nums)
group2, group3 = itertools.tee(group2)
groups = zip(group1, itertools.islice(group2, 1, None), itertools.islice(group3, 2, None))
group1, group2 = itertools.tee(groups)
filtered = filter(lambda args: sum(args[1]) > sum(args[0]), zip(group1, itertools.islice(group2, 1, None)))
agg = functools.reduce(lambda sum, _: sum+1, filtered, 0)
print(agg)
# pdb.set_trace()

# filter(lambda x: x == 2, group_sums)

