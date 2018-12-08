import string
import operator

"""
    FILE INPUT
"""
def getInput(file_loc: str) -> [str]:
    lines = []
    with open(file_loc, 'r') as f:
        lines = f.readlines()
        f.close()
    return lines

def parseLine(line: str) -> (int, int):
    commPos = line.find(',')
    x = int(line[:commPos])
    y = int(line[commPos + 2:])
    return (x, y)

def parseFile(file_loc: str) -> [(int, int)]:
    inp = getInput(file_loc)
    return list(map(parseLine, inp))

"""
    VEC CALC
"""
class VecSpace():
    """ coords   :: (int, int)
        symbols  :: dict {(int, int) -> chr}
        map      :: dict {(int, int) -> (int, int)}
        posStart :: (int, int)
        posEnd   :: (int, int)
    """
    def __init__(self, vecs: [(int, int)]):
        self.coords = vecs
        self.symbols = self.calcSymbols(vecs)
        c = self.calcSpace(vecs)
        self.posStart = c[0]
        self.posEnd = c[1]
        self.map = self.calcMap()
    
    def calcSymbols(self, vecs: [(int, int)]) -> dict:
        symb = {}
        for i in range(0, len(vecs)):
            v = vecs[i]
            symb[v] = string.ascii_letters[i]
        return symb
    
    def calcSpace(self, vecs: [(int, int)]) -> [(int, int)]:
        left = None
        right = None
        top = None
        bot = None
        for v in vecs:
            vx = v[0]
            vy = v[1]
            if left == None:
                left = vx
            else:
                left = vx if vx < left else left

            if right == None:
                right = vx
            else:
                right = vx if vx > right else right

            if top == None:
                top = vy
            else:
                top = vy if vy < top else top
            
            if bot == None:
                bot = vy
            else:
                bot = vy if vy > bot else bot
        return [(left, top), (right, bot)]
    
    def calcMap(self) -> dict:
        mp = {}

        for y in range(self.posStart[1] - 1, self.posEnd[1] + 2):
            for x in range(self.posStart[0] - 1, self.posEnd[0] + 2):
                pos = (x, y)

                bigDist = 10000000
                for v in self.coords:
                    d = self.distTo(v, pos)
                    if d == 0:
                        # self
                        mp[pos] = 0
                        break
                    elif d < bigDist:
                        # closer than another
                        mp[pos] = v
                        bigDist = d
                    elif d == bigDist:
                        # equal distance to another
                        mp[pos] = None
        return mp

    def distTo(self, v1: (int, int), v2: (int, int)) -> int:
        return abs(v2[0] - v1[0] ) + abs(v2[1] - v1[1])

    def isInfinite(self, v1: (int, int)) -> bool:
        nLeft = 0
        nRight = 0
        nAbove = 0
        nBelow = 0
        # there are no vecs on the left
        for x in range(self.posStart[0], v1[0]):
            pos = (x, v1[1])
            if pos in self.map:
                if self.map[pos] != v1:
                    nLeft += 1
        # OR there are no vecs on the right
        for x in range(v1[0], self.posEnd[0]):
            pos = (x, v1[1])
            if pos in self.map:
                if self.map[pos] != v1:
                    nRight += 1
        # OR there are no vecs above
        for y in range(self.posStart[1], v1[1]):
            pos = (v1[0], y)
            if pos in self.map:
                if self.map[pos] != v1:
                    nAbove += 1
        # OR there are no vecs below
        for y in range(v1[1], self.posEnd[1]):
            pos = (v1[0], y)
            if pos in self.map:
                if self.map[pos] != v1:
                    nBelow += 1
        
        return nLeft == 0 or nRight == 0 or nAbove == 0 or nBelow == 0
    
    def numConnected(self, coord: (int, int)) -> int:
        if self.isInfinite(coord):
            return -1
        else:
            n = 0
            for v in self.map:
                if self.map[v] == coord:
                    n += 1
            # for itself
            n += 1
            return n
    
    # (coord, num)
    def mostConnected(self) -> ((int, int), int):
        ns = {}
        for v in self.coords:
            ns[v] = self.numConnected(v)
        sortedNs = sorted(ns.items(), key=operator.itemgetter(1))
        #return (sortedNs.keys(0), sortedNs.keys[0])
        return sortedNs
    
    def distToAllCoords(self, v: (int, int)) -> int:
        d = 0
        for c in self.coords:
            d += self.distTo(v, c)
        return d
    
    def sizeOfSafe(self) -> int:
        n = 0
        for pos in self.map:
            d = self.distToAllCoords(pos)
            if d < 10000:
                n += 1
        return n
    
    def __repr__(self) -> str:
        s = ''
        for y in range(self.posStart[1] - 1, self.posEnd[1] + 2):
            for x in range(self.posStart[0] - 1, self.posEnd[0] + 2):
                pos = (x, y)

                if pos in self.coords:
                    symb = self.symbols[pos]
                    if self.isInfinite(pos):
                        #s += '\033[92m{}\033[0m'.format('I')
                        s += '>'
                    else:
                        #s += '\033[92m{}\033[0m'.format(symb)
                        s += symb
                else:
                    if pos in self.map:
                        val = self.map[pos]
                        
                        if val == None:
                            s += '.'
                        else:
                            s += self.symbols[val]
                    else:
                        s += '-'
            s += '\n'
        return s

"""
    TESTS
"""
def testInputTxt():
    vecs = parseFile('input_tests.txt')

    space = VecSpace(vecs)
    print(space)
    print(vecs)
    print(space.isInfinite(vecs[2]))

def tests():
    testInputTxt()

"""
    MAIN
"""
def task():
    vecs = parseFile('input.txt')
    space = VecSpace(vecs)

    #conn = space.mostConnected()
    #print(list(map(lambda x: (space.symbols[x[0]], x[1]), conn)))

    print(space.sizeOfSafe())

    with open('vecmap.txt', 'w') as f:
        f.write(str(space))
        f.close()

#tests()
task()