def countId(id: str) -> dict:
    counts = {}
    for x in id:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

def countIds(ids: [str]) -> int:
    countTwo = 0
    countThree = 0
    for id in ids:
        hasTwo = False
        hasThree = False

        d = countId(id)
        for x in d:
            am = d[x]
            if am == 2:
                hasTwo = True
            if am == 3:
                hasThree = True
        countTwo += 1 if hasTwo else 0
        countThree += 1 if hasThree else 0
    #print('{} {}'.format(countTwo, countThree))
    return countTwo * countThree

with open('input.txt', 'r') as f:
    lines = f.readlines()
    print(countIds(lines))