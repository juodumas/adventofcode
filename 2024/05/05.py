rules, updates = open(0).read().split("\n\n")
rules = {r for r in rules.split()}
updates = [list(map(int, pages.split(","))) for pages in updates.split()]
s1 = s2 = 0

def is_good(pages):
    return all(f"{p1}|{p2}" in rules for p1, p2 in zip(pages, pages[1:]))

for pages in updates:
    if is_good(pages):
        s1 += pages[len(pages) // 2]
    else:
        while not is_good(pages):
            for i, (p1, p2) in enumerate(zip(pages, pages[1:])):
                if f"{p2}|{p1}" in rules:
                    pages[i] = p2
                    pages[i+1] = p1
        s2 += pages[len(pages) // 2]

print(s1, s2)
