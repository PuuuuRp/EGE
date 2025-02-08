with open('26.txt') as f:
    N = int(f.readline())
    prod = {}
    for i in f:
        art, pr, st = map(int, i.split())
        if art not in prod:
            prod[art] = [pr, 1, st]
        else:
            prod[art][1] += 1
            prod[art][2] += st

sred = sum([i[0] for i in prod.values()]) / len(prod)
ans = [i for i in prod.values() if i[0] > sred]

ans = sorted(ans, key=lambda x: (-x[2], -x[0], x[1]-x[2]))