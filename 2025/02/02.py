def main(f, sum1=0, sum2=0):
    for ids in open(f).read().split(","):
        start, end = map(int, ids.split("-"))
        while start <= end:
            id_str = str(start)
            half = len(id_str) // 2
            if id_str[:half] == id_str[half:]:
                sum1 += start
                sum2 += start
            else:
                for i in range(1, half + 1):
                    if not any(id_str.split(id_str[0:i])):
                        sum2 += start
                        break
            start += 1
    print(sum1, sum2)


main(0)
