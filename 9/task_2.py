class Game():
    """
        circle       :: [int]
        count_marble :: int
        cur_marble   :: int
        last_marble  :: int
 
        players      :: [int]
        num_players  :: int
        pTurn        :: int
    """
    def __init__(self, num_players: int, last_marble: int):
        self.circle = [0]
        self.count_marble = 1
        self.cur_marble = 0
        self.last_marble = last_marble
        self.players = [0] * num_players
        self.num_players = num_players
        self.pTurn = 1
    
    def start(self) -> None:
        for i in range(0, self.last_marble):
            self.place(self.count_marble, self.pTurn)
            self.incPlayerTurn()
            self.count_marble += 1    
            #print(self)
    
    def incPlayerTurn(self):
        nxt = (self.pTurn + 1) % (self.num_players + 1)
        self.pTurn = nxt if nxt != 0 else 1
    
    def incPlayerScore(self, player: int, amnt: int):
        self.players[player - 1] += amnt
    
    def getHighestPlayerScore(self) -> int:
        self.players.sort()
        return self.players[self.num_players - 1]

    def place(self, marble: int, player: int) -> None:
        if marble % 23 == 0:
            # add score of marble player was going to place
            self.incPlayerScore(player, marble)

            # marble 7 marbles cc is added to score
            toRemIdx = self.idxAntiClockwise(self.getCurCircleIdx(), 7)
                #print('\n{}\n'.format(self.circle[toRemIdx]))
            self.incPlayerScore(player, self.circle[toRemIdx])
            # & current = marble clockwise of said marble
            self.cur_marble = self.circle[self.idxClockwise(toRemIdx, 1)]
                #print('\n{}->{}\n'.format(toRemIdx, self.idxClockwise(toRemIdx, 1)))
            # & said marble is removed
            self.circle.remove(self.circle[toRemIdx])
        else:
            idx = self.between((self.idxClockwise(self.getCurCircleIdx(), 1), self.idxClockwise(self.getCurCircleIdx(), 2)))
            self.circle.insert(idx, marble)
            self.cur_marble = marble
    
    def between(self, nextTwoIdx: (int, int)):
        if nextTwoIdx == (0, 0):
            return 1
        elif nextTwoIdx[1] == 0:
            return nextTwoIdx[0] + 1
        else:
            return nextTwoIdx[1]

    def idxClockwise(self, pos: int, amnt: int) -> int:
        return (pos + amnt) % len(self.circle)

    def idxAntiClockwise(self, pos: int, amnt: int) -> int:
        return (pos - amnt) % len(self.circle)

    def getCurCircleIdx(self) -> int:
        return self.circle.index(self.cur_marble)
    
    def reprCircle(self) -> str:
        s = ''
        for x in self.circle:
            if x == self.cur_marble:
                s += '({})\t'.format(x)
            else:
                s += '{}\t'.format(x)
        return s
    
    def __repr__(self) -> str:
        return '[{}]{:2}{}'.format(self.pTurn, '', self.reprCircle())

def parseInput(inp: str) -> (int, int):
    inpS = inp.split(' ')
    plyrs = int(inpS[0])
    lastPnts = int(inpS[6])
    return (plyrs, lastPnts)

def getScoreForGame(g: Game) -> int:
    g.start()
    return g.getHighestPlayerScore()

def getScoreForInput(inp: str) -> int:
    parsed = parseInput(inp)
    return getScoreForGame(Game(parsed[0], parsed[1]))

def tests():
    parsed = parseInput('9 players; last marble is worth 25 points')
    g1 = Game(parsed[0], parsed[1])
    assert g1.between((0, 0)) == 1
    assert g1.between((0, 1)) == 1
    assert g1.between((2, 0)) == 3
    assert g1.between((2, 3)) == 3
    assert g1.between((4, 5)) == 5
    assert g1.between((6, 0)) == 7
    g1.start()
    assert g1.getHighestPlayerScore() == 32

    parsed = parseInput('10 players; last marble is worth 1618 points')
    g2 = Game(parsed[0], parsed[1])
    g2.start()
    assert g2.getHighestPlayerScore() == 8317
    
    parsed = parseInput('13 players; last marble is worth 7999 points')
    g3 = Game(parsed[0], parsed[1])
    g3.start()
    assert g3.getHighestPlayerScore() == 146373

def task():
    base = '465 players; last marble is worth {} points'
    dist = 0
    mp = {}
    c = 0
    for i in range(0, 1500):
        score = getScoreForInput(base.format(i))
        if score != dist:
            c += 1
            diff = score - dist
            dist = score
            iDiff = score - i
            div = i // 465

            if diff in mp:
                mp[diff] = mp[diff] + 1
            else:
                mp[diff] = 1

            print('{}: {} |\t{}|\t{}'.format(i, score, iDiff, diff, ))
            print('\t{}->+{}\t{}'.format(c, diff, mp))
        #print(getScoreForInput(base.format(i)))

    #parsed = parseInput('465 players; last marble is worth 1 points')
    #g = Game(parsed[0], parsed[1])
    #g.start()
    #print(g.getHighestPlayerScore())

#tests()
task()