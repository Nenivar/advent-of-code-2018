def addPos(p1: (int, int), p2: (int, int)) -> (int, int):
    return (p1[0] + p2[0], p1[1] + p2[1])

# ----------------

OPEN = '.'
TREE = '|'
LMBR = '#'

acresStart = {}

with open('input.txt', 'r') as f:
    pos = (0, 0)
    for line in map(lambda x: x.strip(), f.readlines()):
        for c in line:
            acresStart[pos] = c
            pos = addPos(pos, (1, 0))
        pos = addPos(pos, (0, 1))
        pos = (0, pos[1])
    f.close()

class Acres():
    def __init__(self, acresStart: {}):
        self.acres = acresStart
        self.width = 50
        self.height = 50
    
    def getVal(self, pos: (int, int)):
        return self.acres[pos] if pos in self.acres else None
    
    def getNeigh(self, pos: (int, int)) -> {}:
        neigh = {}
        for y in range(-1, 2):
            for x in range(-1, 2):
                coord = addPos(pos, (x, y))
                if coord != pos:
                    neigh[coord] = self.getVal(coord)
        return neigh
    
    def cycle(self):
        newAcre = {}
        for y in range(0, self.height):
            for x in range(0, self.width):
                coord = (x, y)
                val = self.getVal(coord)
                neigh = self.getNeigh(coord)

                nOpen = len(list(filter(lambda x: self.getVal(x) == OPEN, neigh)))
                nTree = len(list(filter(lambda x: self.getVal(x) == TREE, neigh)))
                nLumb = len(list(filter(lambda x: self.getVal(x) == LMBR, neigh)))
                
                newAcre[coord] = val
                if val == OPEN:
                    if nTree > 2:
                        newAcre[coord] = TREE
                elif val == TREE:
                    if nLumb > 2:
                        newAcre[coord] = LMBR
                elif val == LMBR:
                    if nLumb > 0 and nTree > 0:
                        newAcre[coord] = LMBR
                    else:
                        newAcre[coord] = OPEN
        self.acres = newAcre
    
    def getResVal(self) -> int:
        nTree = len(list(filter(lambda x: self.getVal(x) == TREE, self.acres)))
        nLumb = len(list(filter(lambda x: self.getVal(x) == LMBR, self.acres)))
        return nTree * nLumb
    
    def __repr__(self) -> str:
        s = ''
        for y in range(0, self.height):
            for x in range(0, self.width):
                s += self.getVal((x, y))
            s += '\n'
        return s

acres = Acres(acresStart)
print(acres)

for i in range(0, 10):
    acres.cycle()
    print(acres)

print(acres.getResVal())