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

def tests():
    board = [3, 7]
    recipes = Recipes(board)
    print(recipes)
    num = 509671

    for i in range(1, 600000):
        recipes.simRound()
        #print(recipes)
        if len(recipes.board) > num + 10:
            print(recipes.board[num:num + 10])
            break

def task():
    pass

tests()