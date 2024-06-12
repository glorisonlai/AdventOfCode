import pdb
import re

INPUT = 'input.txt'
EXAMPLE = 'example.txt'

def read_coords(file):
    while line := file.readline().strip():
        yield line

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


    def parse(self, instr: str) -> None:
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
        coords = map(lambda line: tuple(map(lambda x: int(x),(line.split(',')))), [line for line in read_coords(in_file)])
        pipeline = Pipeline()
        pipeline.parse(in_file.readline())

    hashset = set()
    for coord in coords:
        hashset.add(pipeline.exec(coord))

    print(len(hashset))
    return len(hashset)


main()
