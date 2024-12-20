from math import sqrt


def viz(coords, paths=[], base_color=36, path_color=41):
    sz = int(sqrt(len(coords)))
    for y in range(sz):
        for x in range(sz):
            v = coords.get(x + 1j * y)
            color = base_color
            for i, path in enumerate(paths):
                if x + 1j * y in path:
                    color = path_color + i
            v = f"\033[0;{color}m{v}\033[0m"
            print(v, end="")
        print()
    print()
