m = [[c for c in line.strip()] for line in open(0)]
sz = len(m)
visits = set()
directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
starti, startj = next(((i, j) for i in range(sz) for j in range(sz) if m[i][j] == '^'))
visits.add((starti, startj))
def solve(pi, pj, visits=set()):
    di = 0
    turns = set()
    while True:
        hi, hj = directions[di]
        if not (0 <= pi + hi < sz and 0 <= pj + hj < sz): return 1
        if m[pi + hi][pj + hj] == '#':
            di = (di + 1) % 4
            if (pi, pj, di) in turns: return 2 # loop
            turns.add((pi, pj, di))
        else:
            pi += hi
            pj += hj
            visits.add((pi, pj))
solve(starti, startj, visits)
obstacles = 0
for i in range(sz):
    for j in range(sz):
        if m[i][j] != '#' and (i, j) != (starti, startj) and (i, j) in visits:
            orig = m[i][j]
            m[i][j] = '#'
            if solve(starti, startj) == 2: obstacles += 1
            m[i][j] = orig
print('visits', len(visits), 'obstacles', obstacles)
