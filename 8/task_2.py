from functools import reduce

class Node():
    """ children     :: [Node]
        num_children :: int
        meta         :: [int]
        num_meta     :: int
    """
    def __init__(self, num_children: int, num_meta: int):
        self.children = []
        self.num_children = num_children
        self.meta = []
        self.num_meta = num_meta
    
    def addChild(self, node):
        if len(self.children) == self.num_children:
            raise Exception('Bad amount of children! {}'.format(self.num_children))
        self.children.append(node)
    
    def addMeta(self, data: int):
        if len(self.meta) == self.num_meta:
            raise Exception('Bad amount of children! {}'.format(self.num_meta))
        self.meta.append(data)

    def value(self) -> int:
        if self.num_children == 0:
            # sum of metadata
            return reduce(lambda x,y: x + y, self.meta)
        else:
            # metadata = indexes to child nodes
            sum = 0
            for i in self.meta:
                if i != 0 and i < self.num_children + 1:
                    sum += self.children[i - 1].value()
            return sum
    
    def __repr__(self):
        return '{} {}'.format(self.meta, self.children)

"""
    INPUT
"""
def nodeCreator(data: [int]):
    return Node(data[0], data[1])

# (remaining data, node created)
def dataToNode(data: [int]) -> ([int], Node):
    #print(data)
    newNode = nodeCreator(data[:2])
    data = data[2:]
    #print('\t', data)

    # children
    for i in range(0, newNode.num_children):
        n = dataToNode(data)
        #print(n)
        data = n[0]
        newNode.addChild(n[1])
    # meta
    for i in range(0, newNode.num_meta):
        newNode.addMeta(data[0])
        data = data[1:]
    
    #print(newNode)
    return (data, newNode)

def sumNode(node: Node) -> int:
    sum = reduce(lambda x,y: x + y, node.meta)
    for n in node.children:
        sum += sumNode(n)
    return sum

def readInput(file_loc: str) -> str:
    s = ''
    with open(file_loc, 'r') as f:
        s = f.readline()
        f.close()
    return s

def inputToData(data: str) -> [int]:
    return list(map(int, data.strip().split(' ')))

"""
    TESTS
"""
def tests():
    lines = readInput('input_tests.txt')
    r = inputToData(lines)
    node = dataToNode(r)[1]
    assert sumNode(node) == 138

    print(node.value())

def task():
    lines = readInput('input.txt')
    r = inputToData(lines)
    node = dataToNode(r)[1]
    #print(sumNode(node))
    print(node.value())

tests()
task()