from functools import cache

devmap = {line.split(":")[0]: line.split()[1:] for line in open(0)}


@cache
def solve(root, fft=False, dac=False, res=0):
    for dev in devmap[root]:
        if dev == "out":
            return res + fft and dac
        res += solve(dev, fft=fft or dev == "fft", dac=dac or dev == "dac")
    return res


if "you" in devmap:
    print(solve("you", True, True))
if "svr" in devmap:
    print(solve("svr"))
