import math


def dist(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


def load(f):
    boxes = {tuple(map(int, line.rstrip().split(","))) for line in open(0)}
    box_pairs = {(dist(*b1, *b2), *sorted((b1, b2))) for b1 in boxes for b2 in boxes if b1 != b2}
    return sorted(list(box_pairs)), boxes


def solve(box_pairs, boxes):
    circuits = []
    box_to_circuit = {}
    part1_max_pairs = 10 if len(boxes) < 1000 else 1000
    for i, (_, b1, b2) in enumerate(box_pairs):
        if i == part1_max_pairs:
            print("part1", math.prod(len(c) for c in sorted(circuits, key=lambda c: -len(c))[:3]))
        b1circuit = box_to_circuit.get(b1)
        b2circuit = box_to_circuit.get(b2)
        if b1circuit and b2circuit and b1circuit != b2circuit:
            for b in b2circuit:
                b1circuit.add(b)
            circuits.remove(b2circuit)
            for box, c in box_to_circuit.items():
                if c == b2circuit:
                    box_to_circuit[box] = b1circuit
        else:
            circuit = b1circuit or b2circuit or set()
            if not circuit:
                circuits.append(circuit)
            circuit.add(b1)
            circuit.add(b2)
            box_to_circuit[b1] = circuit
            box_to_circuit[b2] = circuit
        boxes.discard(b1)
        boxes.discard(b2)
        if not boxes and len(circuits) == 1:
            print("part2", b1[0] * b2[0])
            break


box_pairs, boxes = load(0)
solve(box_pairs, boxes)
