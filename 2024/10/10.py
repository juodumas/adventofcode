coords = {x + 1j * y: int(h) for y, ln in enumerate(open(0)) for x, h in enumerate(ln.strip())}

def go(coord, height, paths=[]):
    if height == 9:
        paths.append(coord)
    for dir in (1 + 0j, 0 + 1j, -1 + 0j, 0 - 1j):
        if coords.get(coord + dir) == height + 1:
            go(coord + dir, height + 1, paths)

paths = {coord: [] for coord in coords}
for coord, height in coords.items():
    if height == 0:
        go(coord, height, paths[coord])

print(sum(len(set(path)) for path in paths.values()), sum(len(path) for path in paths.values()))
