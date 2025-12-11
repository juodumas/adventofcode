def draw(reds, hi1=set(), hi2=set()):
    rows = max(y for _, y in reds) + 2
    cols = max(x for x, y in reds) + 2
    greens = set()
    for i in range(len(reds)):
        x1, y1 = reds[i]
        x2, y2 = reds[i - 1]
        if x1 == x2:
            greens.update((x1, y) for y in range(y1, y2, 1 if y1 < y2 else -1))
        elif y1 == y2:
            greens.update((x, y1) for x in range(x1, x2, 1 if x1 < x2 else -1))

    for y in range(rows):
        for x in range(cols):
            char = "\033[90m•\033[0m"
            if (x, y) in reds:
                char = "\033[91mR\033[0m"
            elif (x, y) in greens:
                char = "\033[92mG\033[0m"
            if (x, y) in hi1:
                char = f"\033[43m{char}\033[0m"
            if (x, y) in hi2:
                char = f"\033[44m{char}\033[0m"
            print(char, end="")
        print()
    print()
