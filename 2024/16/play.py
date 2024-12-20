# pip install pygame
import sys
from math import sqrt

import pygame as pg  # type: ignore
from d16 import find_shortest_path, parse  # type: ignore

WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (220, 0, 0)
COLOR_WALL = (100, 150, 100)
COLOR_END = (200, 200, 0)
COLOR_POS = (0, 220, 0)


def color_temp(count, max_count):
    blue = max(0, 255 - int(255 * (count / max_count)))
    red = min(255, int(255 * (count / max_count)))
    return (red, 0, blue)


def draw_maze(screen, coords, width, height, cellsz):
    for y in range(height):
        for x in range(width):
            v = coords.get(x + 1j * y)
            if v == "#":
                rect = pg.Rect(x * cellsz, y * cellsz, cellsz, cellsz)
                pg.draw.rect(screen, COLOR_WALL, rect)


def draw_point(screen, pos, cellsz, color):
    x = int(pos.real)
    y = int(pos.imag)
    rect = pg.Rect(x * cellsz, y * cellsz, cellsz, cellsz)
    pg.draw.rect(screen, color, rect)


def reset_with_maze(screen, maze, width, height, start, end, cellsz):
    screen.fill(0)
    draw_maze(screen, maze, width, height, cellsz)
    draw_point(screen, start, cellsz, COLOR_POS)
    draw_point(screen, end, cellsz, COLOR_END)


def do_events(wait_for_enter=False):
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                return
        if not wait_for_enter:
            break


def main():
    WIDTH = 1300
    HEIGHT = 1300

    screen_flags = pg.DOUBLEBUF | pg.SCALED

    pg.init()
    pg.event.set_allowed([pg.QUIT])
    pg.key.set_repeat(250, 50)
    screen = pg.display.set_mode([WIDTH, HEIGHT], screen_flags, 16)
    clock = pg.time.Clock()

    def update(wait_for_enter=False):
        pg.display.flip()
        clock.tick(fps)
        do_events(wait_for_enter=wait_for_enter)

    maze, start, end = parse(sys.argv[1] if len(sys.argv) > 1 else 0)
    maze_width = maze_height = int(sqrt(len(maze)))
    cellsz = WIDTH // max(maze_width, maze_height)

    fps = 120
    reset_with_maze(screen, maze, maze_width, maze_height, start, end, cellsz)
    solver = find_shortest_path(maze, start, end)
    last_type = 0
    color_n = 0

    update(True)

    for typ, data in solver:
        if typ == 1:
            weight, path = data
            last_type = typ
            color = color_temp(weight, 100000)
            for pos in path:
                draw_point(screen, pos, cellsz, color)
            update()
        elif typ == 2:
            path = data
            if last_type != typ:
                fps = 60
                reset_with_maze(screen, maze, maze_width, maze_height, start, end, cellsz)
                color_n = 0
            last_type = typ
            for i, pos in enumerate(path):
                color_n += 1
                color = color_temp(i, len(path))
                draw_point(screen, pos, cellsz, color)
                update()
        else:
            update()

    while True:
        do_events()
        clock.tick(fps)


if __name__ == "__main__":
    main()
