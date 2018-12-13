cartChars = {'^', '>', 'v', '<'}
dirs = {'^' : (0, -1), '>' : (1, 0), 'v' : (0, 1), '<' : (-1, 0)}
dirToLeft = {'v' : '>', '^' : '<', '>' : '^', '<' : 'v'}
dirToRight = {'v' : '<', '^' : '>', '>' : 'v', '<' : '^'}
class Cart():
    def __init__(self, x: int, y: int, dir: chr):
        self.x = x
        self.y = y
        self.dir = dir
        self.itsCount = 0
    
    def getPos(self) -> (int, int):
        return (self.x, self.y)
    
    def addPos(self, pos: (int, int)) -> None:
        self.x += pos[0]
        self.y += pos[1]
    
    def getDirVec(self) -> (int, int):
        return dirs[self.dir]
    
    def incrItsCount(self) -> None:
        self.itsCount = (self.itsCount + 1) % 3
    
    def turnLeft(self) -> None:
        self.dir = dirToLeft[self.dir]
    
    def turnRight(self) -> None:
        self.dir = dirToRight[self.dir]
    
    def setItsDir(self) -> None:
        if self.itsCount == 2:
            self.turnRight()
        elif self.itsCount == 1:
            # straight
            pass
        elif self.itsCount == 0:
            self.turnLeft()
    
    def __repr__(self) -> str:
        return self.dir

railChars = {'/', '-', '\\', '|', '-', '+'}
class Track():
    def __init__(self, rails: {}, carts: {}, size=(0, 0)):
        self.rails = rails
        self.carts = carts
        self.size = size
    
    def moveCart(self, cart: Cart) -> None:
        rail = cart.getPos()
        if rail in self.rails:
            if self.rails[rail] == '+':
                cart.setItsDir()
                cart.incrItsCount()
            elif self.rails[rail] == '\\':
                if cart.dir == '>' or cart.dir == '<':
                    cart.turnRight()
                elif cart.dir == '^' or cart.dir == 'v':
                    cart.turnLeft()
            elif self.rails[rail] == '/':
                if cart.dir == '>' or cart.dir == '<':
                    cart.turnLeft()
                elif cart.dir == '^' or cart.dir == 'v':
                    cart.turnRight()
            cart.addPos(cart.getDirVec())
    
    def moveCarts(self) -> None:
        newCarts = {}
        danger = []
        for y in range(0, self.size[1]):
            for x in range(0, self.size[0]):
                coord = (x, y)
                if coord in self.carts:
                    cart = self.carts[coord]
                    self.moveCart(cart)

                    # cart already there - crash!
                    if cart.getPos() in newCarts or cart.getPos() in danger:
                        danger.append(cart.getPos())
                        newCarts.pop(cart.getPos())
                        """ #self.rails[cart.getPos()] = 'X'
                        print('Crash at {}!'.format(cart.getPos()))
                        with open('output.txt', 'w') as f:
                            f.write(str(self))
                            f.close()
                        print(self)
                        input() """
                    else:
                        newCarts[cart.getPos()] = cart
        if len(newCarts) == 1:
            print(newCarts)
            print("Only one cart remaining at: {}".format(list(newCarts.values())[0].getPos()))
            with open('output.txt', 'w') as f:
                f.write(str(self))
                f.close()
            input()
        self.carts = newCarts

    
    def __repr__(self) -> str:
        s = ''
        for y in range(0, self.size[1]):
            for x in range(0, self.size[0]):
                coord = (x, y)
                if coord in self.carts:
                    s += str(self.carts[coord])
                elif coord in self.rails:
                    s += self.rails[coord]
                else:
                    s += ' '
            s += '\n'
        return s

def readInput(file_loc: str) -> [str]:
    lines = []
    with open(file_loc, 'r') as f:
        lines = f.readlines()
        f.close()
    return list(map(lambda x: x, lines))

def parseInput(inp: str) -> Track:
    rails = {}
    carts = {}

    x = 0
    y = 0
    bigX = 0
    for line in inp:
        for val in line:
            coord = (x, y)

            if x > bigX:
                bigX = x

            if val in cartChars:
                carts[coord] = Cart(x, y, val)
                # add correct track char
                if val == '>' or val == '<':
                    rails[coord] = '-'
                elif val == '^' or val == 'v':
                    rails[coord] = '|'
            elif val in railChars:
                rails[coord] = val
            x += 1
        x = 0
        y += 1

    return Track(rails, carts, (bigX + 1, len(inp)))

def tests():
    tr = parseInput(readInput('input_tests3.txt'))

    print(tr)
    for i in range(1, 400):
        print(i)
        tr.moveCarts()
        print(tr)
        input()

def task():
    tr = parseInput(readInput('input.txt'))

    print(tr)
    for i in range(1, 100000):
        print(i)
        """ if i == 1000:
            with open('output.txt', 'w') as f:
                f.write(str(tr))
                f.close()
            input() """
        tr.moveCarts()

task()
#tests()