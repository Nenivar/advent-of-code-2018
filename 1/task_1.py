def parse(line: str) -> int:
    num = int(line[1:])
    return -num if line[0] == '-' else num

with open('input.txt', 'r') as f:
    sum = 0
    for l in f.readlines():
        sum += parse(l)
    f.close()
    print("{}".format(sum))