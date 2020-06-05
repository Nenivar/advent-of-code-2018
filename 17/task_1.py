CLAY = '#'
WATER = ['|', '~', '+']

def parseLine(line: str) -> [(int, int)]:
    poss = []
    vals = line.strip().split(',')
    
    fstAxis = line[0]
    fstVal = int(vals[0][2:])

    rangeVal = list(map(int, vals[1][3:].split('..')))
    for v in range(rangeVal[0], rangeVal[1] + 1):
        if fstAxis == 'x':
            poss.append((fstVal, v))
        else:
            poss.append((v, fstVal))

    return poss

def readInput(file_loc: str) -> {}:
    ground = {}
    with open(file_loc, 'r') as f:
        for line in f:
            for pos in parseLine(line):
                ground[pos] = CLAY
        f.close()
    return ground

def printGround(ground: {}) -> None:
    for y in range(0, 14):
        for x in range(494, 508):
            coord = (x, y)
            if coord in ground:
                print(ground[coord], end='')
            else:
                print('.', end='')
        print('')

ground = readInput('input_tests.txt')
ground[(500, 0)] = WATER[2]

water = [(500, 0)] #: [(int, int)]
printGround(ground)

def addPos(p1: (int, int), p2: (int, int)) -> (int, int):
    return (p1[0] + p2[0], p1[1] + p2[1])

width = 0
height = 0
for g in ground:
    width = g[0] if g[0] > width else width
    height = g[1] if g[1] > height else height

for i in range(0, 4):
    water = {k:v for (k,v) in ground.items() if v in WATER}
    
    for wpos in water:
        down = addPos(wpos, (0, 1))
        if down not in ground:
            ground[down] = WATER[0]
            break
        
        left = addPos(wpos, (-1, 0))
        leftBelow = addPos(left, (0, 1))
        right = addPos(wpos, (1, 0))
        rightBelow = addPos(right, (0, 1))

        # if section closed

        if left not in ground and leftBelow in ground:
            ground[left] = WATER[1]
            break
        elif right not in ground and rightBelow in ground:
            ground[right] = WATER[1]
            break
    
    printGround(ground)
    print('----')

class Tracker():
    def __init__(self, startPos: (int, int)):
        self.pos = startPos
        self.visited = []
    
    def moveBackwards(self) -> None:
        self.pos = self.visited.pop()
    
    def moveTo(self, newPos: (int, int)):
        self.visited.append(self.pos)
        self.pos = newPos
    
    # returns false if it could not move
    def tryMove(self):
        # move down
        down = addPos(self.pos, (0, 1))
        if down not in ground:
            if down[1] > height:
                self.moveBackwards()
                return False
            ground[down] = WATER[0]
            self.moveTo(down)
            return True

        # TODO: left and right
        left = addPos(self.pos, (-1, 0))
        leftBelow = addPos(left, (0, 1))
        right = addPos(self.pos, (1, 0))
        rightBelow = addPos(right, (0, 1))
        # if left & leftBelow == water & 
        if left not in ground:# and leftBelow in ground:
            ground[left] = WATER[1]
            self.moveTo(left)
            return True
        elif right not in ground:# and rightBelow in ground:
            ground[right] = WATER[1]
            self.moveTo(right)
            return True
        else:
            # can't move any more - recurse
            self.moveBackwards()
            self.tryMove()

        return False

""" trck = Tracker((500, 0))
for i in range(0, 55):
    trck.tryMove()
    printGround(ground) """