from math import inf

DIRS = (1, 1j, -1, -1j)
WALL, EMPTY, START, END = '#', '.', 'S', 'E'

class Segment:
    def __init__(self, weight, end_dir):
        self.weight = weight
        self.end_dir = end_dir
        self.path = [] 

def parse(f: str | int=0):
    maze = {x+1j*y: thing for y, ln in enumerate(open(f)) for x, thing in enumerate(ln.strip())}
    start = next(c for c, thing in maze.items() if thing == START)
    end = next(c for c, thing in maze.items() if thing == END)
    return maze, start, end

def go_to_crossroad(maze, pos, mydir, path):
    weight = 1
    visited = set(path)
    while True:
        moves = [pos + d for d in DIRS if maze.get(pos + d) in (EMPTY, END) and pos + d not in visited]
        move_cnt = len(moves)
        if move_cnt >= 2 or maze.get(pos) == END:
            return pos, mydir, weight # reached crossroad
        if move_cnt == 0:
            return None, None, None # deadend
        weight += 1
        if moves[0] != pos + mydir:
            weight += 1000
            mydir = moves[0] - pos
        pos = moves[0]
        visited.add(pos)
        path.append(pos)

def find_shortest_path(maze, start, end, mydir=1):
    queue = {c for c, t in maze.items() if t != WALL and sum(maze.get(c+d) == EMPTY for d in DIRS) >= 3}
    queue.add(start)
    queue.add(end)
    segments = {c: Segment(0, mydir) if c == start else Segment(inf, 0) for c in queue}
    prev = {c: None for c in queue}

    while queue:
        c1 = min((c for c in queue), key=lambda x: segments[x].weight)
        if c1 == end:
            break
        queue.remove(c1)
        start_dir = segments[c1].end_dir
        
        moves = [c1 + d for d in DIRS if maze.get(c1 + d) in (EMPTY, END)]
        for move in moves:
            path = [c1, move]
            c2, end_dir, weight = go_to_crossroad(maze, move, start_dir, path)
            if weight is None or c2 not in queue:
                continue
            weight += segments[c1].weight
            if weight < segments[c2].weight:
                segments[c2].weight = weight
                segments[c2].end_dir = end_dir
                segments[c2].path = path
                prev[c2] = c1
                yield 1, (weight, path) # Dijkstra search
    
    c2 = end
    shortest_path = [end]
    while (c1 := prev[c2]):
        shortest_path.extend(segments[c2].path[::-1][1:])
        c2 = c1
    yield 2, shortest_path[::-1] # shortest path
    yield 0, segments[end].weight # shortest path score

def main(f):
    maze, start, end = parse(f)
    solver = find_shortest_path(maze, start, end)
    for what, result in solver:
        if what == 0:
            print('score', result)

if __name__ == "__main__":
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else 0)
