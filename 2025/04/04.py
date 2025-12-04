def draw(maze):
    from math import sqrt

    size = sqrt(len(maze))
    for coord, thing in maze.items():
        print(thing, end="\n" if coord.real == size - 1 else "")


def solve(maze, removable_paper=False):
    count = 0
    for coord, thing in maze.items():
        if thing != "@":
            continue
        can_remove = sum(
            maze.get(coord + x + y * 1j) == "@"
            for x in range(-1, 2)
            for y in range(-1, 2)
            if not (x == 0 and y == 0)
        ) < 4
        count += can_remove
        if can_remove and removable_paper:
            maze[coord] = '.'
    return count


def main(f, sum1=0, sum2=0):
    maze = {x + y * 1j: thing for y, line in enumerate(open(f)) for x, thing in enumerate(line.strip())}
    sum1 += solve(maze)
    sum2_count = 1
    while sum2_count:
        sum2_count = solve(maze, True)
        sum2 += sum2_count
    print(sum1, sum2)


main(0)
