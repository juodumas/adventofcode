# only part1; part2 "solution" is in 14.js
import math
import re
from collections import Counter

pattern = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)\n"
data = [list(map(int, r)) for r in re.findall(pattern, open(0).read())]
xmax, ymax = 101, 103
xmid, ymid = xmax // 2, ymax // 2
quads = (Counter(), Counter(), Counter(), Counter())
for sec in range(1, 101):
    for i, (px, py, vx, vy) in enumerate(data):
        px += vx
        py += vy
        if px < 0:
            px = xmax + px
        elif px >= xmax:
            px = px - xmax
        if py < 0:
            py = ymax + py
        elif py >= ymax:
            py = py - ymax
        data[i][0] = px
        data[i][1] = py
        if sec == 100:
            if px != xmid and py != ymid:
                q = px // (xmid + 1) + 2 * (py // (ymid + 1))
                quads[q][(px, py)] += 1
print("safety factor", math.prod([q.total() for q in quads]))
