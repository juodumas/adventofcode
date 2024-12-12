def map_area(coord, area):
    if coord in area: return
    area.add(coord)
    for dir in dirs:
        if coords.get(coord + dir) == coords[coord]:
            map_area(coord + dir, area)

coords = {x + 1j * y: c for y, ln in enumerate(open(0)) for x, c in enumerate(ln.strip())}
dirs = (1, 1j, -1, -1j)
visited = set()
price1 = price2 = 0
viz_data = []
for coord, plant in coords.items():
    if coord in visited: continue
    area = set()
    map_area(coord, area)
    visited |= area
    perimeter = []
    sides = {}
    for coord in area:
        for dir in dirs:
            if coords.get(coord + dir) != plant:
                perimeter.append((coord, dir))
                v = (coord.real, dir.real) if dir.real else (coord.imag*1j, dir.imag*1j)
                sides.setdefault(v, [])
                sides[v].append((coord + dir).imag if dir.real else (coord + dir).real)
    side_count = 0
    for values in sides.values():
        values.sort()
        side_count += 1 + sum(abs(a - b) > 1 for a, b in zip(values, values[1:]))
    price1 += len(area) * len(perimeter)
    price2 += len(area) * side_count
    viz_data.append((plant, perimeter))

print(price1, price2)
# from viz import viz; viz(coords, viz_data) # writes viz.html
