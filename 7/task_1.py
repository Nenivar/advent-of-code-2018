import time

"""
    DATA
"""
class Step():
    'A step in the requirements.'
    """ id        :: chr
        linksTo   :: [Step]
        linksFrom :: [Step]
    """
    def __init__(self, id: chr):
        self.id = id
        self.linksTo = []
        self.linksFrom = []
    
    # alphabetically first link
    def firstLinkTo(self):
        return self.linksTo[0]
    
    def addLinkTo(self, to) -> None:
        self.linksTo.append(to)
        self.linksTo.sort()
    
    def addLinkFrom(self, frm) -> None:
        self.linksFrom.append(frm)
        self.linksFrom.sort()

    def reprLinksTo(self) -> str:
        return list(map(lambda x: x.id, self.linksTo))
    
    def reprLinksFrom(self) -> str:
        return list(map(lambda x: x.id, self.linksFrom))
    
    def __lt__(self, other):
        return self.id < other.id

    def __repr__(self) -> str:
        return '{}: {}->{};\t{}<-{}'.format(self.id, self.id, self.reprLinksTo(), self.id, self.reprLinksFrom())

def findFirst(steps: [Step]) -> [Step]:
    return list(filter(lambda s: not s.linksFrom, steps))

def findLast(steps: [Step]) -> Step:
    return list(filter(lambda s: not s.linksTo, steps))[0]

def runThrough(steps: [Step]) -> [Step]:
    marked = []
    avail = [] # :: [Part]
    finished = list(steps.keys())
    finished.sort()

    # there are multiple first nodes
    last = findLast(steps.values())
    first = findFirst(steps.values())
    avail.extend(first[1:])

    # ...but there still needs to be one first
    cur = first[0]
    print('Starting with {}'.format(cur))
    while cur != last:
        marked.append(cur)
        print('current: {}'.format(cur.id))
        print('marked: {}'.format(stepsStr(marked)))
        print('avail: {}'.format(stepsStr(avail)))
        print('-')

        # add all available
        for l in cur.linksTo:
            if l not in avail:
                avail.append(l)
        #avail.extend(cur.linksTo)
        avail.sort()
        print('avail: {}'.format(stepsStr(avail)))

        # get next part w/ all links activated
        c = 0
        nxt = None
        fullyLinked = False
        while not fullyLinked:
            if c < len(avail):
                nxt = avail[c]
                # check if fully linked
                ok = True
                for x in nxt.linksFrom:
                    if x not in marked:
                        ok = False
                if ok:
                    fullyLinked = True
                else:
                    print('\t{} has not satisfied all links!'.format(nxt))
                    c += 1
            else:
                raise Exception('ah!')
        print('next is {}'.format(nxt))
        
        avail.remove(nxt)
        cur = nxt
        print('---')
        #time.sleep(1)
    
    marked.append(last)
    return marked

"""
    INPUT
"""
def getInput(file_loc: str) -> [str]:
    lines = []
    with open(file_loc, 'r') as f:
        lines = f.readlines()
        f.close()
    return lines

def parseLine(line: str) -> (chr, chr):
    f = line.find('p') + 2
    fst = line[f:f + 1]
    s = line.find('step') + 5
    snd = line[s:s + 1]
    return (fst, snd)

# only w/ initial id
def createSteps(parsed: [(chr, chr)]) -> {Step}:
    steps = {}
    for p in parsed:
        steps[p[0]] = Step(p[0])
        if Step(p[1]) not in steps:
            steps[p[1]] = Step(p[1])
    return steps

def createLinks(steps: {Step}, parsed: [(chr, chr)]):
    for p in parsed:
        frm = p[0]
        to = p[1]
        steps[frm].addLinkTo(steps[to])
        steps[to].addLinkFrom(steps[frm])

def runThroughInput(file_loc: str) -> [Step]:
    lines = getInput(file_loc)
    parsed = list(map(parseLine, lines))
    steps = createSteps(parsed)
    createLinks(steps, parsed)
    return runThrough(steps)

"""
    TESTS
"""
def printSteps(steps: [Step]) -> None:
    for s in steps:
        print(steps[s])

def stepsStr(steps: [Step]) -> str:
    return ','.join(list(map(lambda x: x.id, steps)))

def tests():
    print(stepsStr(runThroughInput('input_tests.txt')).replace(',', ''))

"""
    TASK
"""
def task():
    print(stepsStr(runThroughInput('input.txt')).replace(',', ''))

#tests()
task()