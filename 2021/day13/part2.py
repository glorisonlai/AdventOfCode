import pdb
import re

INPUT = 'input.txt'
EXAMPLE = 'example.txt'

def read_line(file):
    while line := file.readline():
        line = line.strip()
        if line: 
            yield line
        else:
            break

class Pipeline:
    def __init__(self):
        self.instructions = []


    class Instruction:
        def __init__(self, hori_fold: bool, fold_at: int):
            self.hori_fold = hori_fold
            self.fold_at = fold_at

        def exec(self, coord: tuple[int, int]) -> tuple[int,int]:
            change_index, keep_index = int(self.hori_fold), int(not self.hori_fold)
            new_coord = [None, None]
            new_coord[keep_index] = coord[keep_index]
            new_coord[change_index] = self.fold_at - abs(coord[change_index] - self.fold_at)
            return tuple(new_coord)


    def parse(self, instrs: list[str]) -> None:
        for instr in instrs:
            matches = re.match(r".*([xy])=([0-9]+)", instr)
            assert matches.group(1)
            assert matches.group(2)
            self._add_instruction(hori_fold = matches.group(1) == 'y', fold_at=int(matches.group(2)))

    def _add_instruction(self, hori_fold: bool, fold_at: int) -> None:
        self.instructions.append(self.Instruction(hori_fold, fold_at))


    def exec(self, coord: tuple[int, int]) -> tuple[int, int]:
        for instr in self.instructions:
            coord = instr.exec(coord)
        return coord


def main():
    with open(INPUT, 'r') as in_file:
        coords = map(lambda line: tuple(map(lambda x: int(x),(line.split(',')))), [line for line in read_line(in_file)])
        pipeline = Pipeline()
        pipeline.parse([line for line in read_line(in_file)])


    hashset = set()
    for coord in coords:
        hashset.add(pipeline.exec(coord))

    dimensions = max(hashset)[0], max(hashset, key=lambda x: x[1])[1]
    for y in range(dimensions[1]+1):
        line = []
        for x in range(dimensions[0]+1):
            line.append('#' if (x,y) in hashset else ' ')
        print(''.join(line))

    print(len(hashset))
    return len(hashset)


main()
