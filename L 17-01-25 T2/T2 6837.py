from itertools import *
def f(x1, x2, x3, x4, x5):
    return (x1 or not x2 or not x3 or x4 or not x5)and \
        (not x1 or not x2 or x3 or x4 or x5)and \
        (x1 or not x2 or not x3 or not x4 or x5)

for a, b, c, d, e in product([0, 1], repeat=5):
    tab = [(0, 1, 1, 0, a), (0, 1, 1, 1, 0), (0, 1, c, d, 1), (0, 0, 0, 1, 0)]
    if len(set(tab)) == len(tab):
        u = [f(*t) for t in tab] == [1, b, 0, e]
        if u: print(a, b, c, d, e)
