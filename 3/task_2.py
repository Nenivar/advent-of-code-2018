class Rect:
    def __init__(self, id: int, x: int, y: int, w: int, h: int):
        self.id = id
        self.pos = (x,y)
        self.size = (w,h)
    def getX(self):
        return self.pos[0]
    def getY(self):
        return self.pos[1]
    def getEndX(self):
        return self.getX() + self.getW()
    def getEndY(self):
        return self.getY() + self.getH()
    def getW(self):
        return self.size[0]
    def getH(self):
        return self.size[1]
    
    def __repr__(self):
        return "{}: {},{} | {},{}".format(self.id, self.getX(), self.getY(), self.getW(), self.getH())

def parse(line: str) -> Rect:
    id = line[1:line.find('@') - 1]
    x = line[line.find('@') + 2:line.find(',')]
    y = line[line.find(',') + 1:line.find(':')]
    w = line[line.find(':') + 2:line.find('x')]
    h = line[line.find('x') + 1:len(line) - 1]
    #print("{},{} | {},{}".format(x, y, w, h))
    return Rect(id, int(x), int(y), int(w), int(h))

with open('input.txt', 'r') as f:
    dict = {}
    lines = f.readlines()
    rects = list(map(parse, lines))

    for r in rects:
        for y in range (r.getX(), r.getEndX()):
            for x in range (r.getY(), r.getEndY()):
                k = (x, y)
                if k in dict:
                    dict[k] = 2
                else:
                    dict[k] = 1

    goodRects = []
    for r in rects:
        # check all area
        # I know x & y are flipped (oops)
        bad = False
        for y in range(r.getX(), r.getEndX()):
            for x in range(r.getY(), r.getEndY()):
                k = (x,y)
                if k in dict and dict[k] > 1:
                    bad = True
                    break
            else:
                continue
            break
        if not bad:
            goodRects.append(r)
        
    for g in goodRects:
        print(g)