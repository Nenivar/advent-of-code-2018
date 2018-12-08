from enum import Enum
import functools
import string

# immutable
class Vec2():
    def __init__(self, x: int, y: int, label=''):
        self.x = x
        self.y = y
        self.label = label
    
    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        if other == None:
            return False
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return '({},{})'.format(self.x, self.y)

    # will never be equal S_W, S_E...
    def isEqDir(self, dir, other):
        flag = True
        if (dir.value.x == 1 or dir.value.x == -1) and self.x != other.x:
            flag = False
        if (dir.value.y == 1 or dir.value.y == -1) and self.y != other.y:
            flag = False
        return flag
    
    def isMoreDir(self, dir, other):
        flag = True
        """ if dir == dir.N_W:
            return self.x < other.x and self.y < other.y
        elif dir == dir.N:
            return self.y < other.y
        elif dir == dir.N_E:
            return self.x > other.x and self.y < other.y
        elif dir == dir.E:
            return self.x > other.x
        elif dir == dir.S_E:
            return self.x > other.x and self.y > other.y
        elif dir == dir.S:
            return self.y > other.y
        elif dir == dir.S_W:
            return self.x < other.x and self.y > other.y
        elif dir == dir.W:
            return self.x < other.x """
        if dir.value.x == 1 and self.x <= other.x:
            flag = False
        if dir.value.x == -1 and self.x >= other.x:
            flag = False
        if dir.value.y == 1 and self.y <= other.y:
            flag = False
        if dir.value.y == -1 and self.y >= other.y:
            flag = False
        return flag
    
    def toTuple(self):
        return (self.x, self.y)

class Rect():
    def __init__(self, pos: Vec2, posEnd: Vec2):
        self.pos = pos
        self.posEnd = posEnd
    
    def isVecIn(self) -> bool:
        pass
    
    def __repr__(self):
        return '({}->{}, {}->{})'.format(self.pos.x, self.posEnd.x, self.pos.y, self.posEnd.y)

class Dir(Enum):
    N_W = Vec2(-1, -1)
    N   = Vec2(0, -1)
    N_E = Vec2(1, -1)
    E   = Vec2(1, 0)
    S_E = Vec2(1, 1)
    S   = Vec2(0, 1)
    S_W = Vec2(-1, 1)
    W   = Vec2(-1, 0)

def getInput(file_loc: str) -> [str]:
    lines = []
    with open(file_loc, 'r') as f:
        lines = f.readlines()
        f.close()
    return lines

def lineToVec2(line: str, label = '') -> Vec2:
    commPos = line.find(',')
    x = int(line[:commPos])
    y = int(line[commPos + 2:])
    return Vec2(x, y, label)

def inputToVec2(input: [str]) -> [Vec2]:
    vecs = []
    for i in range(0, len(input)):
        l = input[i]
        syb = string.ascii_letters[i]
        vecs.append(lineToVec2(l, syb))
    #return list(map(lineToVec2, input))
    return vecs

# list because it can be tied
def findMostDir(coords: [Vec2], dir: Dir) -> [Vec2]:
    most = []
    for v in coords:
        if most == []:
            most.append(v)
        else:
            if dir == Dir.N_E:
                print('{} w/ {}'.format(v, most))
            if v.isEqDir(dir, most[0]):
                most.append(v)
            elif v.isMoreDir(dir, most[0]):
                most = [v]
    return most

# find viable coordinates
def something() -> None:
    pass

# manhattan distance from one coord->another
def distTo(v1, v2) -> int:
    return abs(v2.x - v1.x ) + abs(v2.y - v1.y)

# get space we're working in
def coordSpace(vecs: [Vec2]) -> Rect:
    left = None
    right = None
    top = None
    bot = None
    for v in vecs:
        if left == None:
            left = v.x
        else:
            left = v.x if v.x < left else left

        if right == None:
            right = v.x
        else:
            right = v.x if v.x > right else right

        if top == None:
            top = v.y
        else:
            top = v.y if v.y < top else top
        
        if bot == None:
            bot = v.y
        else:
            bot = v.y if v.y > bot else bot
    return Rect(Vec2(left, top), Vec2(right, bot))
    

# doesn't work
def isAreaInfinite(vec: Vec2, vecs: [Vec2]) -> bool:
    return functools.reduce(lambda x,y: x and y, map(lambda v: vec.x <= v.x, vecs)) \
        or functools.reduce(lambda x,y: x and y, map(lambda v: vec.x >= v.x, vecs)) \
        or functools.reduce(lambda x,y: x and y, map(lambda v: vec.y <= v.y, vecs)) \
        or functools.reduce(lambda x,y: x and y, map(lambda v: vec.y >= v.y, vecs))

# --------------------------------

def printVecs(vecs: [Vec2]) -> str:
    space = coordSpace(vecs)
    fin = ''
    for y in range(space.pos.y - 1, space.posEnd.y + 2):
        for x in range(space.pos.x - 1, space.posEnd.x + 2):
            s = '-'
            v = Vec2(x,y)
            if v in vecs:
                """ if isAreaInfinite(v, vecs):
                    s = 'I'
                else:
                    s = '#' """
                # find v
                for vv in vecs:
                    if v == vv:
                        v = vv
                        break
                if v.label != '':
                    s = v.label
                else:
                    s = '#'
            fin += s
        fin += '\n'
    return fin

def printMap(map: dict, vecs: [Vec2]) -> str:
    space = coordSpace(vecs)
    fin = ''
    for y in range(space.pos.y - 1, space.posEnd.y + 2):
        for x in range(space.pos.x - 1, space.posEnd.x + 2):
            if (x,y) in map:
                s = map[(x, y)]
            else:
                s = '-'
            fin += s
        fin += '\n'
    return fin

def testVec2() -> None:
    assert Vec2(3, 3) + Vec2(0, 0) == Vec2(3, 3)
    assert Vec2(3, 3) + Vec2(1, 0) == Vec2(4, 3)
    assert Vec2(3, 3) + Vec2(-5, 0) == Vec2(-2, 3)

def testDir() -> None:
    assert Vec2(3,3).isMoreDir(Dir.E, Vec2(0,0))
    assert Vec2(3,3).isMoreDir(Dir.S_E, Vec2(0,0))
    assert Vec2(-1,-1).isMoreDir(Dir.W, Vec2(3, 3))
    assert Vec2(-1,-5).isMoreDir(Dir.N_W, Vec2(3, 3))

    assert Vec2(3,3).isEqDir(Dir.W, Vec2(3, 0))
    assert Vec2(2,3).isEqDir(Dir.S, Vec2(0, 3))

def testInput() -> None:
    vecs = inputToVec2(getInput('input_tests.txt'))
    #assert findMostDir(vecs, Dir.N_W) == Vec2(1,1)
    for x in Dir:
        print('{}:  \t{}'.format(x, findMostDir(vecs, x)))
    #assert findMostDir(vecs, Dir.S_W) == Vec2(8,9)
    for v in vecs:
        print('{}: {}'.format(v, isAreaInfinite(v,vecs)))
    print(coordSpace(vecs))
    print(printVecs(vecs))

    space = coordSpace(vecs)
    map = {}
    for y in range(space.pos.y - 1, space.posEnd.y + 1):
        for x in range(space.pos.x - 1, space.posEnd.x + 1):
            pos = Vec2(x, y)

            bigDist = 100000
            for v in vecs:
                d = distTo(v, pos)
                if d == bigDist:
                    map[pos.toTuple()] = '.'
                if d < bigDist:
                    map[pos.toTuple()] = v.label
                    bigDist = d
    print(printMap(map, vecs))

def tests() -> None:
    testVec2()
    testDir()
    testInput()

def task() -> None:
    # dict 'cos we're in 'infinite' space
    map = {}

    vecs = inputToVec2(getInput('input.txt'))

    for v in vecs:
        print('{}: {}'.format(v, isAreaInfinite(v,vecs)))
    print(coordSpace(vecs))
    print(len(vecs))

    space = coordSpace(vecs)
    map = {}
    for y in range(space.pos.y - 1, space.posEnd.y + 1):
        for x in range(space.pos.x - 1, space.posEnd.x + 1):
            pos = Vec2(x, y)

            bigDist = 100000
            for v in vecs:
                d = distTo(v, pos)
                if d == bigDist:
                    map[pos.toTuple()] = '.'
                if d < bigDist:
                    map[pos.toTuple()] = v.label
                    bigDist = d
    #print(printMap(map, vecs))
    with open('vecmap.txt', 'w') as f:
        f.write(printMap(map, vecs))
        f.close()

# --------------------------------

#tests()
task()