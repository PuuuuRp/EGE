for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (x <= y) and (z == (w <= x)) and (not w)
                if f: print(w, x, y, z)