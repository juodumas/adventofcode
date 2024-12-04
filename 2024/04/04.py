s1 = s2 = 0
m = [[c for c in '...' + line.strip() + '...'] for line in open(0)]
fill = [['.'] * len(m[0])] * 3
m = [*fill, *m, *fill]
mviz = [row[:] for row in m]

def viz(*coords, color=31):
    for i, j in coords:
        mviz[i][j] = f'\033[0;{color}m' + mviz[i][j] + '\033[0m'

def check(*coords, words=('XMAS', 'SAMX'), color=None):
    word = ''.join(m[i][j] for i, j in coords)
    if word in words:
        if color: viz(*coords, color=color)
        return 1
    return 0

for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] == '.': continue
        s1 += check([i, j], [i, j+1], [i, j+2], [i, j+3], color=0)
        s1 += check([i, j], [i+1, j], [i+2, j], [i+3, j], color=0)
        s1 += check([i, j], [i+1, j+1], [i+2, j+2], [i+3, j+3], color=31)
        s1 += check([i, j], [i-1, j+1], [i-2, j+2], [i-3, j+3], color=0)
        s2 += check([i, j], [i+1, j+1], [i+2, j+2], [i, j+2], [i+1, j+1], [i+2, j], words=('MASMAS', 'MASSAM', 'SAMSAM', 'SAMMAS'), color=0)
for row in mviz: print(''.join(row))
print(s1, s2)
