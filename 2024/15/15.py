ROBOT, WALL, EMPTY = '@', '#', '.'
BOX, BOXL, BOXR = 'O', '[', ']'

def read(f=0): return open(f).read()
def parse(data):
    coords_str, moves_str = data.split('\n\n')
    coords = {}
    pos = x = y = 0
    for y, line in enumerate(coords_str.split()):
        for x, thing in enumerate(line.strip()):
            coord = x+1j*y
            coords[coord] = thing
            if thing == ROBOT:
                pos = coord
    moves_map = {'>': 1, 'v': 1j, '<': -1, '^': -1j}
    moves = [moves_map[c] for c in moves_str if c != '\n']
    return pos, coords, (x + 1, y + 1), moves

def create_wide_map(pos, coords, width, height):
    coords2 = {}
    for y in range(height):
        thing = None
        for x in range(width * 2):
            thing = coords.get(x // 2 + 1j * y)
            if thing == BOX:
                thing = BOXL if x % 2 == 0 else BOXR
            elif thing == ROBOT and x % 2 != 0:
                thing = EMPTY
            coords2[x + 1j * y] = thing
    return pos + int(pos.real), coords2

def rec_move(coords, who, pos, move):
    coords[pos] = EMPTY
    coords[pos + move] = who

def try_move(coords, pos, move, move_boxes=True):
    thing = coords.get(pos)
    if thing == EMPTY:
        return True
    elif thing == BOX:
        if try_move(coords, pos + move, move):
            rec_move(coords, thing, pos, move)
            return True
    elif thing in (BOXL, BOXR):  # wide box
        if move in (-1, 1):  # left/right
            thing2 = BOXL if move == -1 else BOXR
            assert(coords.get(pos + move) == thing2)
            if try_move(coords, pos + move*2, move):
                rec_move(coords, thing2, pos + move, move)
                rec_move(coords, thing, pos, move)
                return True
        else: # up/down
            if thing == BOXR:
                pos = pos - 1
            assert(coords.get(pos) == BOXL)
            assert(coords.get(pos + 1) == BOXR)
            if try_move(coords, pos + move, move, False) and try_move(coords, pos + 1 + move, move, False):
                if move_boxes:
                    try_move(coords, pos + move, move)
                    try_move(coords, pos + 1 + move, move)
                    rec_move(coords, BOXL, pos, move)
                    rec_move(coords, BOXR, pos + 1, move)
                return True

def solve(coords, moves, pos, width=0, height=0):
    for i, move in enumerate(moves):
        if try_move(coords, pos + move, move, True):
            rec_move(coords, ROBOT, pos, move)
            pos += move
    return coords

def gps(coord): return int(coord.real + 100 * coord.imag)
def sum_box_gps(coords, box=BOX): return sum(gps(coord) for coord, thing in coords.items() if thing == box)

def main():
    pos, coords, (width, height), moves = parse(read())
    pos2, coords2 = create_wide_map(pos, coords, width, height)
    solve(coords, moves, pos)
    solve(coords2, moves, pos2, width*2, height)
    print(sum_box_gps(coords), sum_box_gps(coords2, BOXL))

if __name__ == "__main__":
    main()
