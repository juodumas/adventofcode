data = [[c for c in line.strip()] for line in open(0)]
sz = len(data[0])
anti_p1, anti_p2 = set(), set()
ants = {}
for i, row in enumerate(data):
    for j, ant in enumerate(row):
        if ant != '.':
            ants.setdefault(ant, [])
            ants[ant].append((i, j))
print('\n'.join([f'{ant}: {ants[ant]}' for ant in ants]))
for ant in ants:
    coords = ants[ant]
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            z = 1
            while z < sz:
                a1x = x1 + (z * (x2 - x1))
                a1y = y1 + (z * (y2 - y1))
                a2x = x2 + (z * (x2 - x1)) * -1
                a2y = y2 + (z * (y2 - y1)) * -1
                if a1x >= 0 and a1y >= 0 and a1x < sz and a1y < sz:
                    data[a1x][a1y] = '#'
                    if z == 2: anti_p1.add((a1x, a1y))
                    anti_p2.add((a1x, a1y))
                if a2x >= 0 and a2y >= 0 and a2x < sz and a2y < sz:
                    data[a2x][a2y] = '#'
                    if z == 2: anti_p1.add((a2x, a2y))
                    anti_p2.add((a2x, a2y))
                z += 1
for row in data: print(''.join(row))
print('anti_p1', len(anti_p1), 'anti_p2', len(anti_p2))
