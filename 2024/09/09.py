import sys; sys.setrecursionlimit(50000)
data = open(0).read().strip()
id = 0
diskmap = []

for j in range(0, len(data), 2):
    blocks = int(data[j])
    freespace = int(data[j + 1] if j < len(data) - 1 else 0)
    for b in range(blocks): diskmap.append(str(id))
    for _ in range(freespace): diskmap.append('.')
    id += 1

def defrag(data, starti, endi, autosize=False):
    bs = 1
    if endi <= starti: return data
    if data[endi] != '.':
        if autosize:
            while data[endi-bs] == data[endi]: bs += 1
        for i in range(starti, endi, 1):
            if data[i:i+bs] == ['.'] * bs:
                data[i:i+bs] = data[endi-bs+1:endi+1]
                data[endi-bs+1:endi+1] = ['.'] * bs
                return defrag(data, data.index('.', starti) - 1, endi - bs, autosize)
    return defrag(data, starti, endi - bs, autosize)

data = defrag(diskmap[:], 0, len(diskmap) - 1)
print('cksum1', sum(i * int(b) for i, b in enumerate(data) if b != '.'))
data = defrag(diskmap[:], 0, len(diskmap) - 1, autosize=True)
print('cksum2', sum(i * int(b) for i, b in enumerate(data) if b != '.'))
