def parse(line: str) -> int:
    num = int(line[1:])
    return -num if line[0] == '-' else num

dict = {}
sum = 0

lines = []
found = False

with open('input.txt', 'r') as f:
    lines = f.readlines()
    f.close()

while not found:
    for l in lines:
        val = parse(l)

        if sum in dict:
            print("repeat value: {}".format(sum))
            found = True
            break
        else:
            dict[sum] = 1

        sum += val