def joltme(numbers, start, cnt, joltage=0):
    biggest = max(numbers[start : len(numbers) - cnt + 1])
    start += numbers[start:].index(biggest) + 1
    joltage = joltage * 10 + biggest
    return joltme(numbers, start, cnt - 1, joltage) if cnt > 1 else joltage


def main(f, sum1=0, sum2=0):
    for bats in [list(map(int, line.strip())) for line in open(f)]:
        sum1 += joltme(bats, 0, 2)
        sum2 += joltme(bats, 0, 12)
    print(sum1, sum2)


main(0)
