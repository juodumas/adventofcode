def main(f, count=0, pos=50):
    for r in [int(line[1:]) * (-1 if line[0] == "L" else 1) for line in open(f)]:
        pos = (pos + r) % 100
        count += pos == 0
    print(count)


main(0)
