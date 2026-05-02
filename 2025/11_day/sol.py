from collections.abc import Iterable


def main():
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
        # print(part1(lines))
        print(part2(lines))


def part1(lines: list[str]) -> int:
    edges = {}

    for line in lines:
        edge, dest_ = line.split(":", 1)
        dest = dest_.split(" ")
        edges[edge] = dest

    def dfs(node: str):
        if node == "out":
            return 1
        if not node in edges:
            return 0
        return sum(map(dfs, edges[node]))

    return dfs("you")


def list_op(a: Iterable[bool], b: Iterable[bool], op):
    return op(*zip(a, b))


def part2(lines: list[str]) -> int:
    edges = {}

    for line in lines:
        edge, dest_ = line.split(":", 1)
        dest = dest_.split(" ")
        edges[edge] = dest

    memo: dict[str, tuple[bool, bool]] = {}

    def dfs(node: str, has_fft: bool, has_dac: bool):
        if node == "out":
            return has_fft & has_dac
        if not node in edges:
            return 0
        if node == "fft":
            has_fft = True
        if node == "dac":
            has_dac = True
        return sum(dfs(next_node, has_fft, has_dac) for next_node in edges[node])

    return dfs("svr", False, False)


if __name__ == "__main__":
    main()


def test_part_2():
    test = [
        "svr: aaa bbb",
        "aaa: fft    ",
        "fft: ccc    ",
        "bbb: tty    ",
        "tty: ccc    ",
        "ccc: ddd eee",
        "ddd: hub    ",
        "hub: fff    ",
        "eee: dac    ",
        "dac: fff    ",
        "fff: ggg hhh",
        "ggg: out    ",
        "hhh: out    ",
    ]
    assert part2(test) == 2
