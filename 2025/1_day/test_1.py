from part1 import combo1, combo2

def test_1():
    test_case = [
'L68',
'L30        ',
'R48        ',
'L5         ',
'R60        ',
'L55        ',
'L1         ',
'L99        ',
'R14        ',
'L82        ',
    ]
    rotations = [(e[0], int(e[1:])) for e in test_case]
    # print(rotations)
    assert(combo1(rotations) == 3)

def test_2():
    test_case = [
'L68',
'L30        ',
'R48        ',
'L5         ',
'R60        ',
'L55        ',
'L1         ',
'L99        ',
'R14        ',
'L82        ',
    ]
    rotations = [(e[0], int(e[1:])) for e in test_case]
    # print(rotations)
    assert(combo2(rotations) == 6)

def test_3():
    test_case_1 = [('L', 150)]
    assert(combo2(test_case_1) == 2)

    test_case_2 = [('L', 150), ('R', 100)]
    assert(combo2(test_case_2) == 3)

def test_4():
    test_case_3 = [('L', 50), ('L', 1)]
    assert(combo2(test_case_3) == 1)


