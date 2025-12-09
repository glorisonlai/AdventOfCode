import re

def main():
    with open('input.txt') as f:
        line = f.readline()
        ranges = [(int(f[0]), int(f[1])) for f in (e.split('-') for e in line.split(','))]
        sum_invalid = sum([item for sublist in (invalid_id2(e[0], e[1]) for e in ranges) for item in sublist])
        return sum_invalid

def invalid_id1(start, end):
    ans = []
    while start <= end:
        start_str = str(start)

        if len(start_str) % 2:
            start = 10 ** len(start_str)
            continue
        
        first_half_str = start_str[:(len(start_str) + 1) // 2]
        invalid_id_str = first_half_str + first_half_str
        invalid_id = int(invalid_id_str)

        # Outside of range
        if invalid_id > end:
            break

        if invalid_id >= start:
            ans.append(invalid_id)


        first_half = int(first_half_str)
        next_half = first_half + 1
        next_half_str = str(next_half)
        start_str = next_half_str * 2
        start = int(start_str)
    return ans

def invalid_id2(start, end):
    ans = []
    for num in range(start, end + 1):
        id = str(num)
        for parts in range(2, len(id) + 1):
            if len(id) % parts != 0:
                continue
            match = re.findall(id[:(len(id)//parts)], id)
            if len(match) == parts:
                ans.append(num)
                break
    return ans



if __name__ == '__main__':
    print(main())
