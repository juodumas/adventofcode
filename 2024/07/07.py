from itertools import product

equations = [line.strip().split(": ") for line in open(0)]
s1 = s2 = 0

for testval, values in equations:
    testval = int(testval)
    values = list(map(int, (values.split())))
    opcount = len(values) - 1
    ops1 = product("*+", repeat=opcount)
    for ops in ops1:
        r = values[0]
        for i, op in enumerate(ops):
            r = getattr(r, '__mul__' if op == '*' else '__add__')(values[i + 1])
        if r == testval:
            s1 += testval
            s2 += testval
            break
    else:
        ops2 = product("*+|", repeat=opcount)
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
