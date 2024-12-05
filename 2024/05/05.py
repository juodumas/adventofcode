rules, updates = open(0).read().split("\n\n")
rules = {r for r in rules.split()}
updates = [list(map(int, pages.split(","))) for pages in updates.split()]
s1 = s2 = 0

def is_good(pages):
    printed = set()
    for i in range(1, len(pages)):
        p0 = pages[i - 1]
        p1 = pages[i]
        if f"{p1}|{p0}" in rules or (f"{p0}|{p1}" in rules and p0 in printed):
            return False
    return True

for pages in updates:
    if is_good(pages):
        s1 += pages[len(pages) // 2]
    else:
        good = False
        while not good:
            for i in range(1, len(pages)):
                p0 = pages[i-1]
                p1 = pages[i]
                if f"{p1}|{p0}" in rules:
                    pages[i] = p0
                    pages[i-1] = p1
                    good = is_good(pages)
                    break
        s2 += pages[len(pages) // 2]
print(s1, s2)
