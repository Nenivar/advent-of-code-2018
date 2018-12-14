class Recipes:
    def __init__(self, board: []):
        self.board = board
        self.elfIdx = 0
        self.elf2Idx = 1
    
    def sumDigits(self) -> int:
        return self.board[self.elfIdx] + self.board[self.elf2Idx]
    
    def stepFwd(self, idx: int, amnt: int) -> int:
        return (idx + amnt) % len(self.board)
    
    def simRound(self):
        self.board.extend(getDigits(self.sumDigits()))
        #elfIdx = stepFwd()
        self.elfIdx = self.stepFwd(self.elfIdx, 1 + self.board[self.elfIdx])
        self.elf2Idx = self.stepFwd(self.elf2Idx, 1 + self.board[self.elf2Idx])
    
    def __repr__(self) -> str:
        s = ''
        for i in range(0, len(self.board)):
            val = self.board[i]
            if i == self.elfIdx:
                s += '({})'.format(val)
            elif i == self.elf2Idx:
                s += '[{}]'.format(val)
            else:
                s += ' {} '.format(val)
        s += '\n'
        return s

def getDigits(sum: int) -> int:
    return list(map(int, str(sum)))

def subArrIn(subArr: [], arr: []) -> bool:
    if len(arr) < len(subArr):
        return False
    lenDiff = len(arr) - len(subArr)
    for i in range(0, lenDiff + 1):
        flag = True
        for j in range(0, len(subArr)):
            if subArr[j] != arr[j + i]:
                flag = False
        
        if flag:
            return True

def testSubArr():
    assert subArrIn([1,2,3], [1,2,3,4,5])
    assert not subArrIn([1,2,4], [1,2,3,4,5])
    assert subArrIn([2,3,4], [1,2,3,4,5])
    assert subArrIn([3,4,5], [1,2,3,4,5])
    assert subArrIn([2], [1,2,3,4,5])
    assert subArrIn([1,2,3,4,5], [1,2,3,4,5])
    assert not subArrIn([1,2,3,4,5], [1,2,3])
    assert not subArrIn([1,2,3,4,5], [])
    assert subArrIn([], [])

def tests():
    testSubArr()

    board = [3, 7]
    recipes = Recipes(board)
    print(recipes)

    #find = list(map(int, '2,8,1,0,8,6,2,2,1,1'.split(',')))
    #find = list(map(int, '5,0,9,6,7,1'.split(',')))
    #find = [8,9,0,6,9,1]
    find = list(map(int, '5,9,4,1,4'.split(',')))
    buf = [3,7]

    lenBefore = 2
    for i in range(1, 1000000000):
        recipes.simRound()

        extra = len(recipes.board) - lenBefore
        buf.extend(recipes.board[len(board) - extra:])
        if len(buf) > 7:
            buf = buf[len(buf) - 7:]
        lenBefore = len(recipes.board)

        #print('{}: {}'.format(i, recipes), end='')
        #print('buf diff{}: {}\n'.format(extra, buf))

        if subArrIn(find, buf):
            print('FOUND {} == {} at {}'.format(buf, find, len(recipes.board) - len(find)))
            input()
        """ if len(recipes.board) > num + 10:
            print(recipes.board[num:num + 10])
            break """

def task():
    pass

tests()