def main():
    with open('input.txt') as f:
        lines = f.readlines()
        return(part2(lines))
        ops = lines.pop().split()
        numbers = [[int(e) for e in line.split()] for line in lines]
        return(part1(ops, numbers))

def reduce(fun, arr):
    if not arr:
        raise AssertionError('List is empty')
    arr_iter = iter(arr)
    accum = next(arr_iter)
    for e in arr_iter:
        accum = fun(accum, e)
    return accum

def part1(ops, numbers):
    ops_map = {
        '+': int.__add__,
        '*': int.__mul__
    }

    sum = 0

    for i, arr in enumerate(zip(*numbers)):
        op = ops_map[ops[i]]
        sum += reduce(op, arr)
    return sum

def part2(lines):
    ops_string = lines.pop().rstrip('\n')
    ops_map = {
        '+': int.__add__,
        '*': int.__mul__
    }

    sum = 0
    for i, op_string in enumerate(ops_string):
        if op_string == ' ': continue
        op = ops_map[op_string]
        op_nums = []
        for j in range(i, len(ops_string)):
            num_string = ''.join([line[j] for line in lines]).strip()
            if not num_string:
                break
            op_nums.append(int(num_string))

        # print(op_string, op_nums)
        sum += reduce(op, op_nums)
    return sum



if __name__ == '__main__':
    print(main())

# def test_1():
#     ops = ['+', '+', '*']
#     numbers = [
#         [1,2,3],
#         [2,3,4]
#     ]
#     assert(part1(ops, numbers) == 20)

def test_2():
    test = [
        '11 20',
        ' 3  4',
        '+  * '
    ]
    assert(part2(test) == 14 + 8)

def test_3():
    test = [
'123 328  51 64 ',
' 45 64  387 23 ',
'  6 98  215 314',
'*   +   *   +  ',
    ]
    assert(part2(test) == 3263827)
