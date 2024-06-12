import pdb
from enum import Enum

with open('input.txt', 'r') as f:
	data = list(map(lambda x: x.strip(), f.readlines()))

class Comp(Enum):
	MORE0 = '<'
	EQUAL = '='
	MORE1 = '>'

def split_arr(arr: list[str], index: int) -> tuple[Comp, list[str], list[str]]:
	split_1, split_2 = [], []
	count_1 = 0
	for el in arr:
		if el[index] == '1':
			count_1 += 1
			split_1.append(el)
		else:
			split_2.append(el)
	comp = Comp.EQUAL if count_1 == len(arr) / 2 else Comp.MORE0 if count_1 <= len(arr) // 2 else Comp.MORE1
	return comp, split_1, split_2

comp, oxygen, co2 = split_arr(data, 0)
if comp == comp.MORE0:
	oxygen, co2 = co2, oxygen
	
index = 0
print(oxygen)
while len(oxygen) > 1:
	index += 1
	assert index < len(oxygen[0])
	comp, temp_1, temp_0 = split_arr(oxygen, index)
	match comp:
		case Comp.MORE0: oxygen = temp_0
		case other: oxygen = temp_1
	print(oxygen, comp)

index = 0
while len(co2) > 1:
	index += 1
	assert index < len(co2[0])
	comp, temp_1, temp_0 = split_arr(co2, index)
	match comp:
		case Comp.MORE0: co2 = temp_1
		case other: co2 = temp_0
	# print(co2, comp)

print(oxygen[0], co2[0])

print(int(co2[0], 2) * int(oxygen[0], 2))


