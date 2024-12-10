coords = {x + 1j * y: int(h) for y, ln in enumerate(open(0)) for x, h in enumerate(ln.strip())}

def go(coord, height, peaks=[]):
    if height == 9:
        peaks.append(coord)
    for dir in (1 + 0j, 0 + 1j, -1 + 0j, 0 - 1j):
        if coords.get(coord + dir) == height + 1:
            go(coord + dir, height + 1, peaks)

peaks = {coord: [] for coord in coords}
for coord, height in coords.items():
    if height == 0:
        go(coord, height, peaks[coord])

print(sum(len(set(p)) for p in peaks.values()), sum(len(p) for p in peaks.values()))
