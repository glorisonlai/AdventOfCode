TISSUE = '@'
EMPTY = '.'

def zip_sum(a,b):
    return [x + y for x,y in zip(a,b)]

def main():
    with open('input.txt') as f:
        lines = f.readlines()
        grid = [list(l.strip()) for l in lines]
        return part2(grid)

def part1(grid) -> int:
    y_max = len(grid)
    x_max = len(grid[0])

    ans = 0
    surrounding_mask = [(-1,-1), (-1,0), (-1,1),(0,-1), (0,1),(1,-1), (1,0), (1,1)]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            cell = grid[y][x]
            if cell != TISSUE:
                continue
            surroundings = [(a+y, b+x) for a,b in surrounding_mask if (a + y >= 0 and a + y < y_max and b + x >= 0 and b + x < x_max and grid[a+y][b+x] == TISSUE)]
            # print(surroundings)
            if len(surroundings) < 4:
                ans += 1
            # grid[y][x] = 'x'

    # for l in grid:
    #     print(l)
    return ans

def part2(grid) -> int:
    y_max = len(grid)
    x_max = len(grid[0])
    num_roll_grid = [[0 for _ in range(x_max)] for _ in range(y_max)]

    ans = 0
    stack = []
    seen = set()
    surrounding_mask = [(-1,-1), (-1,0), (-1,1),(0,-1), (0,1),(1,-1), (1,0), (1,1)]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            cell = grid[y][x]
            if cell != TISSUE:
                continue
            surroundings = [(a+y, b+x) for a,b in surrounding_mask if (a + y >= 0 and a + y < y_max and b + x >= 0 and b + x < x_max and grid[a+y][b+x] == TISSUE)]
            num_roll_grid[y][x] = len(surroundings)
            if len(surroundings) < 4:
                stack.append((y,x))

    while len(stack):
        y,x = stack.pop()
        if ((y,x) in seen):
            continue
        num_roll_grid[y][x] = 0
        seen.add((y,x))
        ans += 1
        # for n in num_roll_grid:
        #     print(n)
        # print()
        surroundings = [(a+y, b+x) for a,b in surrounding_mask if (a + y >= 0 and a + y < y_max and b + x >= 0 and b + x < x_max and num_roll_grid[a+y][b+x])]
        for a,b in surroundings:
            num_roll_grid[a][b] -= 1
            if num_roll_grid[a][b] < 4:
                stack.append((a,b))
    # for n in num_roll_grid:
    #     print(n)
    return ans
     

            


            
if __name__ == '__main__':
    print(main())

def test_1():
    grid = [
'..@@.@@@@.',
'@@@.@.@.@@',
'@@@@@.@.@@',
'@.@@@@..@.',
'@@.@@@@.@@',
'.@@@@@@@.@',
'.@.@.@.@@@',
'@.@@@.@@@@',
'.@@@@@@@@.',
'@.@.@@@.@.',
    ]
    grid = [list(l) for l in grid]
    assert(part2(grid) == 43)

def test_2():
    grid = [
'..@@',
'.@@@',
    ]
    grid = [list(l) for l in grid]
    assert(part2(grid) == 5)
