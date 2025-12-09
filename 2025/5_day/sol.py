import re

class Node:
    def __init__(self, val = None):
        self.next: "Node | None" = None
        self.val = val if val is not None else (float('-inf'), float('inf'))

    def add(self, next: "Node"):
        node_next = self.next
        self.next = next
        next.next = node_next


def main():
    with open('input.txt') as f:
        lines = f.readlines()
        ranges = []
        ingredients = []
        for line in lines:
            line = line.strip()
            if m := re.match(r'(\d+)-(\d+)$', line):
                ranges.append([int(e) for e in m.groups()])
            else:
                break
            # elif m := re.match(r'(\d+)$', line):
            #     ingredients.append(int(m.group()))
        return(part2(ranges))

def part1(ranges, ingredients):
    ans = 0
    for ingredient in ingredients:
        for lo,hi in ranges:
            if ingredient >= lo and ingredient <= hi:
                ans += 1
                break
    return ans

def part2(ranges):
    merged_ranges_head = Node()

    for lo,hi in ranges:
        # Traverse LL until:
        # N_p_lo <= lo && N_n_hi >= hi (Or next is None)
            # None: Append (lo,hi)
            # Node:
        # n_lo > hi:
            # append before node
        # n_hi < lo
            # append after node
        # n_lo <= hi && n_lo >= lo:
            # merge node: (lo, n_hi)
        # n_hi <= lo && n_hi <= hi:
            # merge node: (n_lo, hi)
        # n_lo >= lo && n_hi <= hi:
            # Nothing

        
        pointer = merged_ranges_head
        l_node = merged_ranges_head
        r_node = None
        while (pointer.next is not None):
            next = pointer.next
            if next.val[0] <= lo:
                l_range = pointer.next
            if next.val[1] >= hi:
                r_range = pointer.next
            pointer = pointer.next
        if pointer.next is None:
            pointer.add(Node((lo,hi)))








if __name__ == "__main__":
    print(main())

def test_1():
    test = [
'3-5  ',
'10-14',
'16-20',
'12-18',
'     ',
'1    ',
'5    ',
'8    ',
'11   ',
'17   ',
'32   ',
    ]
    ranges = []
    ingredients = []
    for line in test:
        line = line.strip()
        if m := re.match(r'(\d+)-(\d+)$', line):
            ranges.append([int(e) for e in m.groups()])
        elif m := re.match(r'(\d+)$', line):
            ingredients.append(int(m.group()))
    assert(part1(ranges, ingredients) == 3)
    
