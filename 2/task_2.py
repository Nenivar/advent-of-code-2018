def diff(id1: str, id2: str) -> str:
    r = ""
    for i in range(0, len(id1)):
        c1 = id1[i]
        c2 = id2[i]
        if c1 != c2:
            r += c1
    return r

def comm(id1: str, id2: str) -> str:
    r = ""
    for i in range(0, len(id1)):
        c1 = id1[i]
        c2 = id2[i]
        if c1 == c2:
            r += c1
    return r

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for l in lines:
        for l2 in lines:
            c = len(diff(l, l2))
            if c == 1:
                print("{},{}->{}".format(l, l2, comm(l,l2)))