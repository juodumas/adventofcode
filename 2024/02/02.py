def check(levels):
    inc_or_dec = sorted(levels) in (levels, levels[::-1])
    rules = all(1 <= abs(a - b) <= 3 for a, b in zip(levels, levels[1:]))
    return rules and inc_or_dec

sum1 = sum2 = 0
for line in open(0):
    levels = list(map(int, line.split()))
    if check(levels):
        sum1 += 1
        sum2 += 1
    else:
        sum2 += any(check(levels[:i] + levels[i + 1 :]) for i in range(len(levels)))

print(sum1, sum2)
