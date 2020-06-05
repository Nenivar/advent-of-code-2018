import re, sys

#sample = '^ENWWW(NEEE|SSE(EE|N))SSWE(S|)$'
sample = '^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$'
#sample = '^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$'

regex = re.compile(r'(\w+)')
bracketed = re.compile(r'\((\w*\|?)*\)')
final = re.compile(r'^((\)|\|)*\$)')
#bracketed = re.compile(r'\(([^()]|(\R?))*\)')

#match = re.search(regex, sample)
#remaining = sample[match.end():]
#print('"{}", "{}"'.format(match.group(1), remaining))

#match = re.search(bracketed, remaining)
#print(match.group(1))
#remaining = sample[match.end():]

# only for outer-most
def findWord(line: str) -> (str, str):
    res = re.search(regex, line)
    if res:
        return (res.group(1), line[res.end():])
    else:
        return ('', line)

# returns (result, str-result)
def findBracketed(line: str) -> (str, str):
    depth = 0
    for i in range(0, len(line)):
        c = line[i]
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
            if depth == 0:
                return (line[1:i], line[i + 1:])
    return ('', line)

def parseLine(line: str) -> []:
    validStrings = []
    word = findWord(line)
    if re.search(final, line) == None:
        print(word[0])
        validStrings.append(word[0])

        if word[1][0] == ')':
            return validStrings
        elif word[1][0:2] == '|)':
            return validStrings
        elif word[1][0] == '|':
            parseLine(word[1])
        else:
            parseLine(word[1])
    else:
        #print('final', line)
        print(validStrings)
        #return validStrings

#print(remaining)
#print(findBracketed(remaining))

#match = re.search(bracketed, remaining)
#print(match.group(0))

print(sample)

#sys.setrecursionlimit(100)
parseLine(sample)

#while sample != '$':
#for i in range(0, 11):
""" depth = 0
while re.search(final, sample) == None:
    word = findWord(sample)
    sample = word[1]
    print('[{}, {}]'.format(word[0], sample))

    if sample[0] == '(':
        depth += 1
    elif sample[0] == ')':
        depth -= 1
    elif sample[0:2] == '|)':
        # add 'or just move on' option
        depth -= 1
    elif sample[0] == '|':
        pass """
    #brckt = findBracketed(sample)
    #sample = brckt[1]
    #print(brckt[0])
    #word = findWord(sample)
    #sample = word[1]
    #print(word[0])