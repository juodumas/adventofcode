class Machine:
    def __init__(self, line):
        spl = line.split()
        self.light_expected = int(spl[0][1:-1].replace(".", "0").replace("#", "1"), 2)
        self.light_count = len(spl[0][1:-1])
        self.buttons = []
        for btn_str in spl[1:-1]:
            idxs = list(map(int, btn_str[1:-1].split(",")))
            self.buttons.append([1 if i in idxs else 0 for i in range(self.light_count)])
        self.buttons_bin = [int("".join(map(str, btns)), 2) for btns in self.buttons]
        self.joltage_expected = tuple(map(int, spl[-1][1:-1].split(",")))

    def solve_light(self):
        min_presses = float("inf")
        explored = set([0])
        queue = [(0, 0)]
        while queue:
            light, presses = queue.pop(0)
            if light == self.light_expected:
                min_presses = min(presses, min_presses)
                continue
            for btn in self.buttons_bin:
                new_light = light ^ btn
                if presses + 1 < min_presses and new_light not in explored:
                    explored.add(new_light)
                    queue.append((new_light, presses + 1))
        return min_presses

    def solve_counters(self):
        target = self.joltage_expected
        cnt = len(target)
        initial = (0,) * len(target)
        min_presses = float("inf")
        explored = set(initial)
        queue = [(initial, 0)]
        level = 0
        while queue:
            counts, presses = queue.pop(0)
            if counts == target:
                min_presses = min(presses, min_presses)
                continue
            for bi, btn in enumerate(self.buttons):
                new_counts = tuple(c + btn[i] for i, c in enumerate(counts))
                if presses + 1 < min_presses and new_counts not in explored:
                    if any(new_counts[i] > target[i] for i in range(cnt)):
                        continue
                    explored.add(new_counts)
                    queue.append((new_counts, presses + 1))
            level += 1
        return min_presses

    def __repr__(self):
        r = [f"[{bin(self.light_expected)[2:]:>0{self.light_count}}]"]
        for x in list(map(lambda b: bin(b)[2:], self.buttons_bin)):
            r.append(f"{x:>0{self.light_count}}")
        r.append(f"{{{','.join(map(str, self.joltage_expected))}}}")
        return " ".join(r)


machines = [Machine(line) for line in open(0)]
sum1 = sum2 = 0

for i, m in enumerate(machines):
    sum1 += m.solve_light()
    # part 2 too slow
    # sum2 += m.solve_counters()

print("sum1", sum1)
print("sum2", sum2)
