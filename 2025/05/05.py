def main(f, sum1=0, sum2=0):
    fresh, ings = open(f).read().strip().split("\n\n")
    ranges0 = sorted([list(map(int, line.split("-"))) for line in fresh.split("\n")])
    ranges = [ranges0[0]]
    for start, end in ranges0[1:]:
        prev_range = ranges[-1]
        if start <= prev_range[1]:
            prev_range[1] = max(prev_range[1], end)
        else:
            ranges.append([start, end])
    for ing in map(int, ings.split("\n")):
        sum1 += any(ing >= r[0] and ing <= r[1] for r in ranges)
    sum2 = sum(end - start + 1 for start, end in ranges)
    print(sum1, sum2)


main(0)
