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

def reactPolyMany(poly: str) -> str:
    polyNew = poly
    changed = True
    while (changed):
        lenPrev = len(polyNew)
        polyNew = reactPoly(polyNew)
        changed = lenPrev != len(polyNew)
    return polyNew

def task() -> None:
    with open('input.txt', 'r') as f:
        line = f.readline()

        r = reactPolyMany(line)
        # why is it len(r) - 1 ??
        print('|{}| = {}'.format(r, len(r) - 1))

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

def test() -> None:
    testReaction()
    testReactPoly()
    testReactPolyMany()

test()
task()