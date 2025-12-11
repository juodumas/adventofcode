# part 1 only
reds = list(tuple(map(int, line.split(","))) for line in open(0))
print(max((x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1 in reds for x2, y2 in reds if x1 != x2 and y1 != y2))
