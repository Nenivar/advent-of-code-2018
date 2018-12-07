import string

def isReaction(c1: chr, c2: chr) -> bool:
    return c1 != c2 and (c1 == c2.lower() or c1 == c2.upper())

# reacts w/ the first it sees
def reactPoly(poly: str) -> str:
    r = ''
    for i in range(0, len(poly)):
        if i == len(poly) - 1:
            r += poly[i]
            break
        else:
            fst = poly[i]
            snd = poly[i + 1]

            if not isReaction(fst, snd):
                r += fst
            else:
                r += poly[i + 2:]
                break
    return r
# i may have looked online for an idea how to do this
# previous func was taking a VERY long time
def reactPolyMany(poly: str) -> str:
    if poly == '':
        return ''

    buf = []
    buf.append(poly[:1])

    #print('--')
    for c in poly[1:]:
        #print(buf)
        if buf == []:
            buf.append(c)
        else:
            if isReaction(c, buf[-1]):
                #print('\tpop {}'.format(c))
                buf.pop()
            else:
                #print('append {}'.format(c))
                buf.append(c)
    return ''.join(buf)

""" def reactPolyMany(poly: str) -> str:
    polyNew = poly
    changed = True
    while (changed):
        lenPrev = len(polyNew)
        polyNew = reactPoly(polyNew)
        changed = lenPrev != len(polyNew)
    return polyNew """

def removeUnit(poly: str, unit: chr) -> str:
    poly = poly.replace(unit.upper(), '')
    return poly.replace(unit.lower(), '')

def task() -> None:
    with open('input.txt', 'r') as f:
        line = f.readline()

        #r = reactPolyMany(line)
        # why is it len(r) - 1 ??
        #print('|{}| = {}'.format(r, len(r) - 1))
        smallestLen = 1000000000000
        for c in string.ascii_lowercase:
            r = removeUnit(line, c)
            r = reactPolyMany(r)

            lenR = len(r)
            print('len when removing {}: {}'.format(c, lenR))
            if lenR < smallestLen:
                smallestLen = lenR
        print(smallestLen)

        #r = removeUnit(line, 'a')
        #r = reactPolyMany(r)
        #print(r)

        f.close()

def testReaction() -> None:
    assert isReaction('a','A') == True
    assert isReaction('a','a') == False
    assert isReaction('a','b') == False
    assert isReaction('b','B') == True
    assert isReaction('B','b') == True

def testReactPoly() -> None:
    assert reactPoly('aA') == ''
    assert reactPoly('Aa') == ''
    assert reactPoly('abBA') == 'aA'
    assert reactPoly('abcBA') == 'abcBA'
    assert reactPoly('abcCBA') == 'abBA'
    assert reactPoly('aAbB') == 'bB'
    assert reactPoly('aabAAB') == 'aabAAB'

def testReactPolyMany() -> None:
    assert reactPolyMany('aA') == ''
    assert reactPolyMany('aAbB') == ''
    assert reactPolyMany('aAcbB') == 'c'
    assert reactPolyMany('aAcCbB') == ''
    assert reactPolyMany('aAcB') == 'cB'
    assert reactPolyMany('dabAcCaCBAcCcaDA') == 'dabCBAcaDA'
    assert reactPolyMany('ppPjJfFLlNtTyYKjJTtkSMmYysAgGTexwWXEJSsjtiIaFf') == 'pN'
    assert reactPolyMany('ppPjJfFLlNtTyYKjJTtkSMmYysAgGTexwWXEJSsjtiIaFfbQqLlhHBDwWdnUuUuN') == 'pN'

def testRemoveUnit() -> None:
    assert removeUnit('aA', 'a') == ''
    assert removeUnit('aAbaaAAa', 'a') == 'b'
    assert removeUnit('aAbaaAAbbBa', 'a') == 'bbbB'
    assert removeUnit('dabAcCaCBAcCcaDA', 'a') == 'dbcCCBcCcD'

def test() -> None:
    testReaction()
    testReactPoly()
    testReactPolyMany()
    testRemoveUnit()

#test()
task()