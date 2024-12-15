import curses
import sys
from curses import KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_UP

from d15 import BOXL, BOXR, ROBOT, create_wide_map, parse, read, rec_move, try_move


def draw(win, coords, width, height, colors):
    for y in range(height):
        for x in range(width):
            v = coords.get(x + 1j * y)
            color = colors["bg"]
            if v == ROBOT:
                color = colors["robot"]
            elif v in (BOXL, BOXR):
                color = colors["box"]
            win.addstr(y, x, v, color)
    win.refresh()


def main(win):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    win.clear()

    colors = {
        "bg": curses.color_pair(1),
        "robot": curses.color_pair(2),
        "box": curses.color_pair(3),
    }
    keys = {KEY_DOWN: 1j, KEY_UP: -1j, KEY_LEFT: -1, KEY_RIGHT: 1}
    key = ""

    pos, coords, (width, height), moves = parse(read(sys.argv[1]))
    pos, coords = create_wide_map(pos, coords, width, height)
    draw(win, coords, width * 2, height, colors)
    move = 0
    while True:
        if move:
            if try_move(coords, pos + move, move, True):
                rec_move(coords, ROBOT, pos, move)
                pos += move
            draw(win, coords, width * 2, height, colors)

        key = win.getch()
        if key in (27, ord("q")):
            return
        move = keys.get(key)


curses.wrapper(main)
