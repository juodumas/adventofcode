from functools import cache

@cache
def blink(stone, i):
    if i == 0:
        return 1
    l = len(str(stone))
    if l % 2 == 0:
        m = 10 ** (l // 2)
        return blink(stone // m, i - 1) + blink(stone % m, i - 1)
    else:
        return blink(1, i - 1) if stone == 0 else blink(stone * 2024, i - 1)

stones = list(map(int, open(0).read().split()))
print(sum(blink(stone, 25) for stone in stones), sum(blink(stone, 75) for stone in stones))
