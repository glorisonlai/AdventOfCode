from collections import deque


# Parses "[.##.]"
# Little endian ([..#] -> 001 (BE) -> 100 (LE) -> 4)
def parse_target(target: str) -> int:
    bit_target = 0
    for i in range(1, len(target) - 1):
        if target[i] == "#":
            bit_target ^= 2 ** (i - 1)
    return bit_target


# Parses "(1,3)" to int
def parse_button(button_str: str) -> int:
    button = 0
    for char in button_str:
        try:
            button ^= 2 ** int(char)
        except ValueError:
            pass
    return button


# Parse "{1,2,3}" to [1,2,3]
def parse_ints(joltage_str: str) -> list[int]:
    return list(map(int, joltage_str[1:-1].split(",")))


def parse_button_mask(length: int, button_str: str) -> list[0 | 1]:
    mask = [0] * length
    for i in parse_ints(button_str):
        mask[i] = 1
    return mask


def main():
    with open("input.txt") as f:
        lines = f.readlines()
        # print(part1(lines))
        print(part2(lines))


def flood_fill(goal: int, paths: list[int]):
    queue = deque([(0, 0)])
    seen = set()
    while len(queue):
        state, iters = queue.popleft()
        seen.add(state)
        for path in paths:
            next_state = state ^ path
            if next_state == goal:
                return iters + 1
            if not next_state in seen:
                queue.append((next_state, iters + 1))
    return -1


def part1(lines: list[str]) -> int:
    machines = []
    for line in lines:
        target_str, *buttons_str, _joltage_str = line.strip().split(" ")
        target = parse_target(target_str)
        buttons = [parse_button(button_str) for button_str in buttons_str]
        machines.append((target, buttons))
    steps = [flood_fill(*machine) for machine in machines]
    return sum(steps)


def sum_list(list_a: list[int], list_b: list[int]) -> list[int]:
    return [a + b for a, b in zip(list_a, list_b)]


def min_joltage_path(start: list[int], button_mask: list[list[int]]) -> int:
    target = [0] * len(start)
    nodes = {str(start): 0}
    check_nodes = deque([start])
    while len(check_nodes):
        cur_node = check_nodes.popleft()
        path_len = nodes[str(cur_node)]
        if cur_node == target:
            return path_len
        next_nodes = [sum_list(cur_node, [-x for x in mask]) for mask in button_mask]
        for next_node in next_nodes:
            if str(next_node) in nodes:
                # We've already seen next node,
                # since our search pattern is BFS, next_node is in a path longer than what we have found
                continue
            if -1 in next_node:
                continue
            if any(x < 0 for x in next_node):
                raise Exception(next_node)

            check_nodes.append(next_node)
            nodes[str(next_node)] = path_len + 1

    return -1


def part2(lines: list[str]) -> int:
    machines = []
    for line in lines:
        _, *buttons_str, joltage_str = line.strip().split(" ")
        joltage = parse_ints(joltage_str)
        buttons = [
            parse_button_mask(len(joltage), button_str) for button_str in buttons_str
        ]
        machines.append((joltage, buttons))
    steps = []
    for i, machine in enumerate(machines):
        print(f"{(i/len(machines)) * 100:.1f}%", machine)
        steps.append(min_joltage_path(*machine))
    return sum(steps)


if __name__ == "__main__":
    main()


def test_flood_fill_1():
    assert flood_fill(6, [8, 10, 4, 12, 5, 3]) == 2
    assert flood_fill(8, [29, 12, 17, 7, 30]) == 3
    assert flood_fill(46, [31, 25, 55, 6]) == 2


def test_parse_target():
    assert parse_target("[.##.]") == 6  # 0110 -> 6
    assert parse_target("[...#.]") == 8  # 00010 -> 01000 -> 8
    assert parse_target("[#.##.]") == 13  # 10110 -> 01101 -> 13


def test_parse_buttons():
    assert parse_button("(3)") == 8
    assert parse_button("(1,3)") == 10
    assert parse_button("(2)") == 4
    assert parse_button("(2,3)") == 12


def test_parse_ints():
    assert parse_ints("(1,2,3,4)") == [1, 2, 3, 4]
    assert parse_ints("(10,11)") == [10, 11]


def test_parse_button_mask():
    assert parse_button_mask(4, "(3)") == [0, 0, 0, 1]
    assert parse_button_mask(4, "(1,3)") == [0, 1, 0, 1]
    assert parse_button_mask(4, "(2)") == [0, 0, 1, 0]
    assert parse_button_mask(4, "(2,3)") == [0, 0, 1, 1]
    assert parse_button_mask(11, "(0,10)") == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]


def test_min_joltage_path():
    machine = [
        [3, 5, 4, 7],
        list(
            map(
                lambda e: parse_button_mask(4, e),
                "(3) (1,3) (2) (2,3) (0,2) (0,1)".split(" "),
            )
        ),
    ]
    assert min_joltage_path(*machine) == 10

    machine = [
        [7, 5, 12, 7, 2],
        list(
            map(
                lambda e: parse_button_mask(5, e),
                "(0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4)".split(" "),
            )
        ),
    ]
    assert min_joltage_path(*machine) == 12

    machine = [
        [10, 11, 11, 5, 10, 5],
        list(
            map(
                lambda e: parse_button_mask(6, e),
                "(0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2)".split(" "),
            )
        ),
    ]
    assert min_joltage_path(*machine) == 11

    machine = [
        [10000, 10000],
        list(
            map(
                lambda e: parse_button_mask(2, e),
                "(0) (0,1) (1)".split(" "),
            )
        ),
    ]
    assert min_joltage_path(*machine) == 10000
