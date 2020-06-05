def addPos(x: (int, int), y: (int, int)) -> (int):
    return (x[0] + y[0], x[1] + y[1])

dirs = {'UP':(0, -1), 'DOWN':(0, 1), 'RGT':(1, 0), 'LFT':(-1, 0)}
class Unit():
    def __init__(self, race: chr, pos: (int, int)):
        self.race = race
        self.pos = pos
        self.ap = 3
        self.hp = 200
        self.game = None
    
    def takeTurn(self) -> None:
        # identify all possible targets
        enemies = self.game.getEnemyUnits(self.race)
        if not enemies:
            # combat ends
            pass
        
        adj = self.getAdjOpenSquares()
        adjEnemies = {k: v for k, v in enemies.items() if k in adj}
        if adjEnemies:
            # attack
            pass
        else:
            # check if any open squares; no -> end turn
            # yes ->
            
            # move to get in range
            pass
    
    def getAdjOpenSquares(self) -> [(int, int)]:
        poss = []
        for d in dirs.values():
            poss.append(addPos(d, self.pos))
        return poss
    
    def __repr__(self) -> str:
        return self.race

class Game():
    def __init__(self, map: [str], units: {Unit}):
        self.map = map
        self.units = units
        for u in self.units.values():
            u.game = self
    
    def __repr__(self) -> str:
        s = ''
        for y in range(0, len(self.map)):
            for x in range(0, len(self.map[y])):
                coord = (x, y)
                if coord in self.units:
                    s += self.units[coord].race
                else:
                    s += self.map[y][x]
            s += '\n'
        return s
    
    def getEnemyUnits(self, friendly: chr) -> {}:
        opp = 'G' if friendly == 'E' else 'E'
        return {k: v for k, v in self.units.items() if v.race == opp}
        """ for coord in self.units:
            if self.units[coord].race == opp
        return list(filter(lambda x: x.race == opp, list(self.units.values()))) """
    
    def simTurn(self):
        for u in self.units.values():
            u.takeTurn()
    
    def getSquare(self, coord: (int, int)) -> chr:
        if coord[0] < len(self.map[0]) and coord[1] < len(self.map):
            return self.map[coord[0]][coord[1]]
        else:
            return None
    
    def getPathTo(self, frm: (int, int), to: (int, int)) -> bool:
        pass

def readInput(file_loc: str) -> Game:
    lines = []
    map = []
    units = {}
    with open(file_loc, 'r') as f:
        lines = f.readlines()
        f.close()
    
    for y in range(0, len(lines)):
        map.append([])
        for x in range(0, len(lines[y])):
            val = lines[y][x]
            if val == '#' or val == '.':
                map[y].append(val)
            elif val == 'G' or val == 'E':
                map[y].append('.')
                units[(x, y)] = Unit(val, (x, y))
    return Game(map, units)

def tests():
    g = readInput('input_tests.txt')
    print(g)
    g.simTurn()

def task():
    pass

tests()