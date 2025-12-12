data = open(0).read().rstrip().split("\n\n")
shapes = [shape[3:] for shape in data[:-1]]
regions = [
    (*map(int, region.split(":")[0].split("x")), *map(int, region.split(": ")[1:][0].split()))
    for region in data[-1].split("\n")
]
sum1 = 0
for x, y, *counts in regions:
    space = x * y
    for idx, count in enumerate(counts):
        space -= shapes[idx].count("#") * count
    sum1 += space >= 0
print("sum1", sum1)
