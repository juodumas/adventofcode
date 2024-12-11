from functools import cache

@cache
def blink(stone, i):
    if i == 0:
        return 1
    if (l := len(str(stone))) % 2 == 0:
        m = 10 ** (l // 2)
        return blink(stone // m, i - 1) + blink(stone % m, i - 1)
    else:
        return blink(stone * 2024 if stone else 1, i - 1)

stones = list(map(int, open(0).read().split()))
print(sum(blink(stone, 25) for stone in stones), sum(blink(stone, 75) for stone in stones))
