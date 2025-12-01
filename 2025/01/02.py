def main(f, count=0, pos=50):
    for r in [int(line[1:]) * (-1 if line[0] == "L" else 1) for line in open(f)]:
        for _ in range(abs(r)):
            pos = (pos + 1 if r > 0 else pos - 1) % 100
            count += pos == 0
    print(count)


main(0)
