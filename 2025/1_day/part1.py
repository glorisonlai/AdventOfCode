def main():
    with open('input.txt') as f:
        lines = f.readlines()
        rotations = [(e[0], int(e[1:])) for e in lines]
        ans = combo2(rotations)
        return ans

def combo2(rotations):
    dial = 50
    modulo = 100
    ans = 0

    for [dir, mag] in rotations:
        pass_0 = mag // modulo
        rem_mag = mag % modulo
        if rem_mag:
            new_dial = (dial - rem_mag if dir == 'L' else dial + rem_mag)

            if dial and (new_dial <= 0 or new_dial >= modulo):
                pass_0 += 1
            dial = new_dial % modulo
        ans += pass_0
        print(dial, pass_0, ans)
    return ans

def combo1(rotations):
    dial = 50
    modulo = 100
    ans = 0

    for [dir, mag] in rotations:
        dial = (dial - mag if dir == 'L' else dial + mag) % modulo
        if dial == 0:
            ans += 1
    return ans

if __name__ == '__main__':
    print(main())
