from functools import reduce


def sq_cart_dist(p1, p2):
    return sum((a - b) ** 2 for a, b in zip(p1, p2))


def main():
    with open("input.txt") as f:
        lines = f.readlines()
        points = [
            (int(a), int(b), int(c))
            for line in lines
            if line.strip()
            for a, b, c in [line.split(",")]
        ]
        # print(part1(points, 1000))
        print(part2(points))


def calc_distances(points: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    points_dist = []
    for i in range(len(points)):
        p_a = points[i]
        for j in range(i + 1, len(points)):
            p_b = points[j]
            points_dist.append((sq_cart_dist(p_a, p_b), i, j))
    return points_dist


def part1(points: list[tuple[int, int, int]], joins: int):
    distances = sorted(calc_distances(points))
    shortest_wires = distances[:joins]

    # Initialise parents
    parents = {}
    for _, i, j in shortest_wires:
        parents[i] = [i, 1]
        parents[j] = [j, 1]

    # Union join
    for _, i, j in shortest_wires:
        union_join(parents, i, j)

    top_3 = sorted([e[1] for e in parents.values()], reverse=True)[:3]
    return reduce(lambda x, y: x * y, top_3)


def part2(points: list[tuple[int, int, int]]):
    distances = sorted(calc_distances(points))
    n = len(points)

    # Initialise parents
    parents = {}
    for _, i, j in distances:
        parents[i] = [i, 1]
        parents[j] = [j, 1]

    for _, i, j in distances:
        parent = union_join(parents, i, j)
        if parents[parent][1] == n:
            return points[i][0] * points[j][0]

    raise Exception("Could not join into single circuit")


def find_parent(parents, i):
    if parents[i][0] == i:
        return i
    return find_parent(parents, parents[i][0])


def union_join(parents, i, j):
    parent_i, parent_j = find_parent(parents, i), find_parent(parents, j)
    if parent_i == parent_j:
        return parent_i
    # Merge groups
    parents[parent_j][0] = parent_i
    # Update sizes
    parents[parent_i][1] += parents[parent_j][1]
    parents[parent_j][1] = 1
    return parent_i


if __name__ == "__main__":
    main()


def test_1():
    wires = [
        (1, 2, 2),
        (3, 4, 4),
        (5, 6, 6),
    ]
    assert part2(wires) == 15


def test_2():
    wires = [
        (162, 817, 812),
        (57, 618, 57),
        (906, 360, 560),
        (592, 479, 940),
        (352, 342, 300),
        (466, 668, 158),
        (542, 29, 236),
        (431, 825, 988),
        (739, 650, 466),
        (52, 470, 668),
        (216, 146, 977),
        (819, 987, 18),
        (117, 168, 530),
        (805, 96, 715),
        (346, 949, 466),
        (970, 615, 88),
        (941, 993, 340),
        (862, 61, 35),
        (984, 92, 344),
        (425, 690, 689),
    ]
    assert part2(wires) == 25272
