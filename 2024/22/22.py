def mix_prune(a, b): return (a ^ b) % 16777216

def monkey_rng(n):
    prev_price = None
    for _ in range(2000):
        n = mix_prune(n, n * 64)
        n = mix_prune(n, int(n / 32))
        n = mix_prune(n, n * 2048)
        price = n % 10
        delta = 0 if prev_price is None else price - prev_price
        prev_price = price
        yield n, price, delta

def main(f):
    numbers = [int(n) for n in open(f)]
    seqs = {}
    s1 = 0
    for n in numbers:
        seq = []
        seen = set()
        for i, (n, price, delta) in enumerate(monkey_rng(n)):
            seq.append(delta)
            if len(seq) > 4:
                seq.pop(0)
                seq_t = tuple(seq)
                seqs.setdefault(seq_t, 0)
                if seq_t not in seen:
                    seqs[seq_t] += price
                    seen.add(seq_t)
            if i == 2000 - 1:
                s1 += n
    print('s1', s1)
    print('s2', max(seqs.values()))

if __name__ == "__main__":
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else 0)
