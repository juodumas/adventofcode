import re

data = re.findall(r"(\d+)\s+(\d+)\n", open(0).read())
data = list(map(sorted, zip(*[(int(x), int(y)) for x, y in data])))
print("p1", sum(abs(a - b) for a, b in zip(*data)))
print("p2", sum(a * data[1].count(a) for a in data[0]))
