def main():
    with open('input.txt') as f:
        lines = f.readlines()
        batteries = [e.strip() for e in lines]
        return(sum(part2(bank) for bank in batteries))

def part1(bank) -> int:
    first, second = '0', '0'
    for i in range(len(bank) - 1):
        if first < bank[i]:
            first = bank[i]
            second = bank[i + 1]
        elif second < bank[i + 1]:
            second = bank[i + 1]

    return int(first + second)

def part2(bank) -> int:
    n = len(bank)
    ans = 0
    last_pos = -1
    for pos in range(12):
        curr_max_joltage = 0
        for bank_i in range(last_pos + 1, min(pos + (n - 12 + 1), n)):
            curr_joltage = int(bank[bank_i])
            if curr_joltage > curr_max_joltage:
                curr_max_joltage = curr_joltage
                last_pos = bank_i
        ans = ans * 10 + curr_max_joltage
    return ans
            

if __name__ == '__main__':
    print(main())

def test_1():
    test = [
'987654321111111',
'811111111111119',
'234234234234278',
'818181911112111',
    ]
    assert(sum(part2(bank) for bank in test) == 3121910778619)

def test_2():
    test = '987654321111111'
    assert(part2(test) == 987654321111)

def test_3():
    test = '811111111111119'
    assert(part2(test) == 811111111119)

def test_4():
    test = '234234234234278'
    assert(part2(test) == 434234234278)

def test_5():
    test = '818181911112111'
    assert(part2(test) == 888911112111)

