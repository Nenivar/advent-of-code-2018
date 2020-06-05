from operations import funcs

opcodes = {'addr': funcs[0], 'addi': funcs[1], \
           'mulr': funcs[2], 'muli': funcs[3], \
           'banr': funcs[4], 'bani': funcs[5], \
           'borr': funcs[6], 'bori': funcs[7], \
           'setr': funcs[8], 'seti': funcs[9], \
           'gtir': funcs[10], 'gtri': funcs[11], 'gtrr': funcs[12], \
           'eqir': funcs[13], 'eqri': funcs[14], 'eqrr': funcs[15]}
        
ipIdx = None
instructions = []

# -> (func, a, b, c)
def parseLine(line: str) -> ():
    params = line.split(' ')
    return (opcodes[params[0]], int(params[1]), int(params[2]), int(params[3]))

with open('input.txt', 'r') as f:
    lines = f.readlines()

    ipIdx = int(lines[0].split(' ')[1])
    instructions = list(map(parseLine, lines[1:]))

    f.close()

#registers = [0] * 6
registers = [1] + [0] * 5
#print(registers)

def executeInstr(instructions: [()]) -> [int]:
    dist = []
    while registers[ipIdx] > -1 and registers[ipIdx] < len(instructions):
        # get next to exec. from pointer.
        next = instructions[registers[ipIdx]]
        next[0](registers, next[1], next[2], next[3])
        # increase pointer
        registers[ipIdx] += 1
        print(registers)

        if registers[0] not in dist:
            #print(registers)
            print(registers[0])
            dist.append(registers[0])
    registers[ipIdx] -= 1

executeInstr(instructions)
print(registers)