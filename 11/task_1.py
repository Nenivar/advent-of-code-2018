class Fuel:
    def __init__(self, serial: int):
        self.serial = serial
        self.cells = {}
        self.w = 300
        self.h = 300

    def getCellPower(self, pos: (int, int)) -> int:
        if pos[0] > 300 or pos[1] > 300:
            return 0
        else:
            if pos in self.cells:
                return self.cells[pos]
            else:
                rackId = pos[0] + 10
                powerLevel = rackId * pos[1]
                powerLevel += self.serial
                powerLevel *= rackId
                powerLevel = getHundDigit(powerLevel)
                powerLevel -= 5
                self.cells[pos] = powerLevel
                return powerLevel

    def get3x3Power(self, startPos: (int, int)) -> int:
        tot = 0
        for y in range(0, 3):
            for x in range(0, 3):
                tot += self.getCellPower((startPos[0] + x, startPos[1] + y))
        return tot
    
    def findMaxPower(self) -> (int, int):
        max = None
        maxCoord = None
        for y in range(0, self.h):
            for x in range(0, self.w):
                p = self.get3x3Power((x, y))
                if max == None:
                    max = p
                    maxCoord = (x, y)
                else:
                    if p > max:
                        max = p
                        maxCoord = (x, y)
        return maxCoord

def getHundDigit(val: int) -> int:
    # prob. slow
    s = str(val // 100)
    return int(s[len(s) - 1:])

def tests():
    assert getHundDigit(15) == 0
    assert getHundDigit(300) == 3
    assert getHundDigit(3100) == 1
    assert getHundDigit(12345) == 3
    assert Fuel(8).getCellPower((3, 5)) == 4
    assert Fuel(39).getCellPower((217, 196)) == 0
    assert Fuel(18).get3x3Power((33, 45)) == 29
    assert Fuel(18).findMaxPower() == (33, 45)

def task():
    print(Fuel(4151).findMaxPower())

#tests()
task()