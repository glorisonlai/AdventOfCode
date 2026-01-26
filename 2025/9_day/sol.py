from functools import reduce


def main():
    with open("input.txt") as f:
        lines = f.readlines()
        coords = [tuple(map(int, line.split(","))) for line in lines]
        print(part1(coords))


def area(p1, p2):
    dim_diffs = [abs(a - b) + 1 for a, b in zip(p1, p2)]
    return reduce(lambda x, y: x * y, dim_diffs)


def part1(coords: list[tuple[int, ...]]) -> int:
    max_area = 0
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            max_area = max(area(coords[i], coords[j]), max_area)
    return max_area


def part2(coords: list[tuple[int, ...]]) -> int:
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            max_area = max(area(coords[i], coords[j]), max_area)


if __name__ == "__main__":
    main()


def test_1():
    coords = [
        (0, 0),
        (0, 2),
    ]
    assert part1(coords) == 3


def test_2():
    coords = [
        (0, 0),
        (1, 1),
        (2, 2),
    ]
    assert part1(coords) == 9


def test_3():
    coords = [
        (7, 1),
        (11, 1),
        (11, 7),
        (9, 7),
        (9, 5),
        (2, 5),
        (2, 3),
        (7, 3),
    ]
    assert part1(coords) == 50
