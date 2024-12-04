import re

data = open(0).read()
matches = re.findall(r"(do|don't)\(\)|mul\((\d+,\d+)\)", data)
s1 = s2 = 0
do = True
for inst, mul in matches:
    if inst == 'do':
        do = True
    elif inst == "don't":
        do = False
    elif mul:
        a, b = map(int, mul.split(","))
        s1 += a * b
        if do:
            s2 += a * b

print(s1, s2)
