coords = {
    x + 1j * y: int(height)
    for y, line in enumerate(open(0))
    for x, height in enumerate(line.strip())
}

def go(coord, height, peaks=set(), paths=[], fork=False):
    if height == 9: peaks.add(coord)
    paths[-1].append(coord)
    saved_path = paths[-1].copy()
    fork = False
    for dir in (1 + 0j, 0 + 1j, -1 + 0j, 0 - 1j):
        if coords.get(coord + dir) == height + 1:
            if fork: paths.append(saved_path.copy())
            go(coord + dir, height + 1, peaks, paths, fork=fork)
            fork = True

paths = []
s1 = 0
for coord, height in coords.items():
    if height: continue
    paths.append([])
    peaks = set()
    go(coord, height, peaks, paths)
    if peaks: s1 += len(peaks)

# from viz import viz; viz(coords, paths[0])
print(s1, sum(1 for path in paths if len(path) == 10))
