import re


def main(f):
    p1, p2 = open(f).read().split("\n\n")
    states = {gate: int(value) for gate, value in re.findall(r"([xy]\d\d): (\d)", p1)}
    instructions = re.findall(r"(\w+) (AND|OR|XOR) (\w+) -> (\w+)", p2)
    found = False
    while not found:
        found = True
        for g1, instr, g2, g3 in instructions:
            if g1 not in states or g2 not in states:
                found = False
                continue
            v1 = states.get(g1, 0)
            v2 = states.get(g2, 0)
            if instr == 'AND':
                states[g3] = v1 & v2
            elif instr == 'OR':
                states[g3] = v1 | v2
            elif instr == 'XOR':
                states[g3] = v1 ^ v2
    r = [states[g] for g in sorted(states)[::-1] if g.startswith('z')]
    binary = ''.join(map(str, r))
    # print('\n'.join([f'{g}: {states[g]}' for g in sorted(states)]))
    print(binary, int(binary, 2))


if __name__ == "__main__":
    import sys

    main(sys.argv[1] if len(sys.argv) > 1 else 0)
