from sol import invalid_id1, invalid_id2

def test_0():
    examples = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224, 1698522-1698528,446443-446449,38593856-38593862,565653-565659, 824824821-824824827,2121212118-2121212124'
    ranges = [(int(f[0]), int(f[1])) for f in (e.split('-') for e in examples.split(','))]
    invalid_ids = [invalid_id2(e[0], e[1]) for e in ranges]
    print(invalid_ids)
    sum_invalid = sum([item for sublist in invalid_ids for item in sublist])
    assert(sum_invalid == 4174379265)

def test_2():
    assert(invalid_id2(95, 115) == [99, 111])


