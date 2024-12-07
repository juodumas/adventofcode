from itertools import product

equations = [line.strip().split(": ") for line in open(0)]
s1 = s2 = 0

def calc(values, ops):
    r = values[0]
    for i, op in enumerate(ops):
        if op == '|': r = int(f'{r}{values[i + 1]}')
        elif op == '+': r += values[i + 1]
        elif op == '*': r *= values[i + 1]
    return r

for testval, values in equations:
    testval = int(testval)
    values = list(map(int, (values.split())))
    opcount = len(values) - 1
    for ops in product("*+", repeat=opcount):
        if calc(values, ops) == testval:
            s1 += testval
            s2 += testval
            break
    else:
        for ops in product("*+|", repeat=opcount):
            if calc(values, ops) == testval:
                s2 += testval
                break
print(s1, s2)
