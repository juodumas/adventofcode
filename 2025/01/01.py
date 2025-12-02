def main(f, sum1=0, sum2=0, pos=50):
    for r in [int(line[1:]) * (-1 if line[0] == "L" else 1) for line in open(f)]:
        for _ in range(abs(r)):
            pos = (pos + 1 if r > 0 else pos - 1) % 100
            sum2 += pos == 0
        sum1 += pos == 0
    print(sum1, sum2)


main(0)
