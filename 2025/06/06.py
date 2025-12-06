import math


def part1(lines, sum1=0):
    data = list(zip(*[line.split() for line in lines]))
    for task in data:
        if task[-1] == "*":
            sum1 += math.prod(map(int, task[:-1]))
        else:
            sum1 += sum(map(int, task[:-1]))
    print("part1", sum1)


def part2(lines, sum2=0):
    action = ""
    c0d3 = "0"
    for col in list(zip(*lines)):
        if number := "".join(x for x in col[:-1] if x.strip()):
            col_action = col[-1].strip()
            if col_action:
                action = col_action
                c0d3 = c0d3[:-1] + "+"
            c0d3 += number + action
    print("part2", eval(c0d3[:-1]))


lines = [line.rstrip("\n") for line in open(0)]
part1(lines)
part2(lines)
