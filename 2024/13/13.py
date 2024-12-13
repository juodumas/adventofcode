import re

pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
price1 = price2 = 0
for coords in re.findall(pattern, open(0).read()):
    ax, ay, bx, by, px, py = map(int, coords)
    for n in (0, 10e12):
        ap = ((px + n) * by - (py + n) * bx) / (ax * by - ay * bx)
        bp = ((px + n) * ay - (py + n) * ax) / (ay * bx - ax * by)
        if ap.is_integer() and bp.is_integer():
            if n == 0:
                price1 += int(ap * 3 + bp)
            else:
                price2 += int(ap * 3 + bp)
print(price1, price2)
