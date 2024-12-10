from math import sqrt


def viz(coords, path=set(), color=31):
    sz = int(sqrt(len(coords)))
    for y in range(sz):
        for x in range(sz):
            height = coords.get(x + 1j * y)
            if x + 1j * y in path:
                height = f"\033[0;{color}m{height}\033[0m"
            print(height, end="")
        print()
    print()
