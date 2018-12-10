class Point():
    """ pos :: (int, int)
        vel :: (int, int)
    """
    def __init__(self, pos: (int, int), vel: (int, int)):
        self.pos = pos
        self.vel = vel
    
    def addVel(self) -> None:
        self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])
    
    def distTo(self, other) -> int:
        return abs(other.pos[1] - self.pos[1]) + abs(other.pos[0] - self.pos[0])
    
    def __repr__(self) -> str:
        return 'pos: {}, vel: {}'.format(self.pos, self.vel)

def letterIntoPoints(letterArr: [str]) -> [(int, int)]:
    points = []
    x = 0
    y = 0
    for line in letterArr:
        for s in line:
            if s == '#':
                points.append((x, y))
            x += 1
        y += 1
        x = 0
    return points

class Sky():
    """ points: [Point]
    """
    def __init__(self, points: [Point]):
        self.points = points
    
    def simRound(self) -> None:
        for p in self.points:
            p.addVel()
    
    def letterExists(self, letterPoints: [(int, int)]) -> bool:
        pass

    def calcCloseness(self) -> int:
        point = self.points[0]
        tot = 0
        for p in self.points:
            tot += point.distTo(p)
        return tot / len(self.points)
    
    def __repr__(self) -> str:
        s = ''
        # only for test input
        startX = self.points[0].pos[0]
        startY = self.points[0].pos[1]
        for y in range(startX - 100, startX + 100):
            for x in range(startY - 100, startY + 100):
                exists = False
                char = '.'
                for p in self.points:
                    if p.pos == (x, y):
                        char = '#'
                s += char
            s += '\n'
        return s

def parseSec(sec: str) -> (int, int):
    l = list(map(lambda s: int(s.strip()), sec.split(',')))
    return (l[0], l[1])

def parseLine(line: str) -> Point:
    pos_s = line.find('<') + 1
    pos_e = line.find('>')
    vel_s = line.find('<', pos_e) + 1
    vel_e = line.find('>', pos_e + 1)
    pos = parseSec(line[pos_s:pos_e])
    vel = parseSec(line[vel_s:vel_e])
    return Point(pos, vel)

def getParsedInput(file_loc: str) -> [Point]:
    return list(map(parseLine, getInput(file_loc)))

def getInput(file_loc: str) -> [str]:
    lines = []
    with open(file_loc, 'r') as f:
        lines = f.readlines()
        f.close()
    return lines

def writeSkyToFile(sky: Sky, file_loc: str) -> None:
    with open(file_loc, 'w') as f:
        f.write(sky.__repr__())
        f.close()

def testLetter():
    letter = ['#.#', \
              '###', \
              '#.#']
    ps = letterIntoPoints(letter)
    assert ps == [(0, 0), (2, 0), \
                  (0, 1), (1, 1), (2, 1), \
                  (0, 2), (2, 2)]

def tests():
    testLetter()

    inp = getParsedInput('input_tests.txt')
    sky = Sky(inp)
    for i in range(0, 5):
        print('{} seconds; closeness: {}:'.format(i, sky.calcCloseness()))
        print(sky)
        sky.simRound()

# inspect until it works haha
def task():
    inp = getParsedInput('input.txt')
    sky = Sky(inp)
    for i in range(0, 11000):
        # found by looking at all all where closeness <= 100
        if i == 10333:
            closeness = sky.calcCloseness()
            print('{} seconds; closeness: {}:'.format(i, closeness))
            if closeness <= 100:
                print(sky)
            writeSkyToFile(sky, 'sky.txt')
        sky.simRound()

#tests()
task()