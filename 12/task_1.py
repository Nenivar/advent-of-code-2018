class Garden():
    def __init__(self, initState: str, rules: {}):
        self.state = initState
        self.rules = rules
        self.startIdx = 0
    
    # adds padding to left & right
    def addPadding(self, amnt: int):
        self.state = '.' * amnt + self.state + '.' * amnt
        self.startIdx += amnt

    def simGen(self) -> None:
        temp = ''
        for i in range(0, len(self.state)):
            start = max(0, i - 2)
            section = self.state[start : i + 3]
            if section in self.rules:
                temp += self.rules[section]
            else:
                temp += '.'
        self.state = temp
    
    def sumGen(self) -> int:
        tot = 0
        for i in range(0, len(self.state)):
            worth = i - self.startIdx
            tot += 0 if self.state[i] == '.' else worth
        return tot
    
    def __repr__(self) -> str:
        s = ''
        for i in range(0, len(self.state)):
            x = self.state[i]
            s += x
        return s

"""
    INPUT
"""
def parseInputInit(line: str) -> str:
    return line[line.find(':') + 2:].strip()

def parseInputRules(lines: [str]) -> {}:
    psd = {}
    for l in lines:
        ls = l.strip().split(' ')
        psd[ls[0]] = ls[2]
    return psd

def parseInput(file_loc: str) -> (str, str):
    init = None
    rules = None
    with open(file_loc, 'r') as f:
        lines = f.readlines()
        init = parseInputInit(lines[0])
        rules = parseInputRules(lines[2:])
        f.close()
    return (init, rules)

"""
    EXEC
"""
def tests():
    psd = parseInput('input_tests.txt')

    g = Garden(psd[0], psd[1])
    g.addPadding(20)
    for i in range(0, 20):
        print('{}:\n{}'.format(i, g))
        g.simGen()
    print(g.sumGen())

def task():
    psd = parseInput('input.txt')
    
    g = Garden(psd[0], psd[1])
    g.addPadding(20)
    for i in range(0, 20):
        print('{}:\n{}'.format(i, g))
        g.simGen()
    print(g.sumGen())

#tests()
task()