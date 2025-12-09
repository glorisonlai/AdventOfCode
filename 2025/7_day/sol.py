EMPTY = '.'
SPLIT = '^'

def main():
    with open('input.txt') as f:
        lines = f.readlines()
        return part2(lines)

def part1(lines):
    beams = set([lines[0].index("S")])
    splits = 0
    for line_i in range(1, len(lines)):
        line = lines[line_i]
        next_beams = set()
        for beam in beams:
            if line[beam] == EMPTY:
                next_beams.add(beam)
            elif line[beam] == SPLIT:
                next_beams.add(max(0, beam - 1))
                next_beams.add(min(len(lines) - 1, beam + 1))
                splits += 1
        # splits += len(next_beams) - len(beams)
        beams = next_beams
    return splits

def part2(lines):
    beams = {lines[0].index("S"): 1}
    for line_i in range(1, len(lines)):
        line = lines[line_i]
        next_beams = {}
        for beam in beams:
            if line[beam] == EMPTY:
                next_beams[beam] = next_beams.get(beam, 0) + beams[beam]
            elif line[beam] == SPLIT:
                l_beam = max(0, beam - 1)
                next_beams[l_beam] = next_beams.get(l_beam, 0) + beams[beam]
                r_beam = min(len(lines), beam + 1)
                next_beams[r_beam] = next_beams.get(r_beam, 0) + beams[beam]

        beams = next_beams
    # Split is collisions * 2 + non_collisions

    splits = sum([beams[i] for i in beams])
    return splits

if __name__ == '__main__':
    print(main())

def test_1():
    test = [
".......S.......",
"...............",
".......^.......",
"...............",
"......^.^......",
"...............",
".....^.^.^.....",
"...............",
"....^.^...^....",
"...............",
"...^.^...^.^...",
"...............",
"..^...^.....^..",
"...............",
".^.^.^.^.^...^.",
"...............",
    ]
    assert(part2(test) == 40)

def test_2():
    test = [
".......S.......",
"...............",
".......^.......",
    ]
    assert(part2(test) == 2)

def test_3():
    test = [
".......S.......",
"...............",
".......^.......",
"...............",
"......^........",
    ]
    assert(part2(test) == 3)
