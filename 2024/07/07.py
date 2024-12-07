from functools import cache
from itertools import combinations

equations = [line.strip().split(": ") for line in open(0)]
operators1 = "*+"
operators2 = "*+|"
s1 = s2 = 0

@cache
def comb(operators, opcount):
    return set(combinations(operators * opcount, opcount))

for testval, values in equations:
    testval = int(testval)
    values = list(map(int, (values.split())))
    opcount = len(values) - 1
    ops1 = comb(operators1, opcount)
    ops2 = comb(operators2, opcount)
    for ops in ops1:
        r = values[0]
        for i, op in enumerate(ops):
            r = getattr(r, '__mul__' if op == '*' else '__add__')(values[i + 1])
        if r == testval:
            s1 += testval
            break
    for ops in ops2:
        r = values[0]
        for i, op in enumerate(ops):
            if op == '|':
                r = int(f'{r}{values[i + 1]}')
            else:
                r = getattr(r, '__mul__' if op == '*' else '__add__')(values[i + 1])
        if r == testval:
            s2 += testval
            break
print(s1, s2)
