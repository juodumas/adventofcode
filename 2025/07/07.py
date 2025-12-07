from collections import Counter


def main(f, sum1=0):
    grid = open(f).read().splitlines()
    beams = Counter([(grid[0].index("S"), 1)])
    for y in range(1, len(grid) - 1):
        beams_new = Counter()
        for (x, _), cnt in beams.items():
            if grid[y + 1][x] == "^":
                sum1 += 1
                beams_new[(x - 1, y + 1)] += cnt
                beams_new[(x + 1, y + 1)] += cnt
            else:
                beams_new[(x, y + 1)] += cnt
        beams = beams_new

    print("sum1", sum1)
    print("sum2", sum(beams.values()))


main(0)
