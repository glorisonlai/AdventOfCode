import pdb
with open('input.txt', 'r') as f:
	data = f.readlines()

gamma, epsilon = 0, 0
bit_length = len(data[0]) - 1
# pdb.set_trace()
for i in range(bit_length):
	gamma <<= 1
	epsilon <<= 1
	count_1 = sum(x[i] == '1' for x in data)
	if count_1 > len(data) // 2:
		gamma += 1
	else:
		epsilon += 1

print(gamma * epsilon)
