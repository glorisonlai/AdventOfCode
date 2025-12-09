def is_safe(nums: list[int]) -> bool:
    i = 1
    prev = nums[0]
    while i < len(nums):
        if nums[i]
    return True 


def main() -> int:
    ans = 0
    with open('input.txt') as f:
        for line in f.readlines():
            nums = [int(e) for e in line.split(' ')]
            if is_safe(nums):
                ans += 1
    return ans




if __name__ == '__main__':
    print(main())
