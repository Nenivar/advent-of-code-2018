from datetime import datetime
import operator

class Guard:
    def __init__(self, id: int):
        self.id = id
        self.sleeps = []
    
    def addSleep(self, sleep: (int, int, int)) -> None:
        #print("\tadding sleep of duration {}".format(sleep[2]))
        self.sleeps.append(sleep)
    
    def getTotSleep(self) -> int:
        tot = 0
        for s in self.sleeps:
            tot += s[2]
        return tot
    
    def getAvgMin(self) -> int:
        mins = {}
        for s in self.sleeps:
            begin = s[0]
            end = s[1]
            for m in range(begin, end):
                if m in mins:
                    mins[m] = mins[m] + 1
                else:
                    mins[m] = 1
        return max(mins.items(), key=operator.itemgetter(1))[0]

    def getStats(self) -> str:
        return 'id:{}, tot:{}, min:{}'.format(self.id, self.getTotSleep(), self.getAvgMin())

    def __str__(self):
        return '{}: {}'.format(self.id, list(map(lambda x: '{}->{}'.format(x[0], x[1]), self.sleeps)))

def parseLine(line: str) -> (datetime, str):
    # parse datetime
    str_dt = line[:line.find(']') + 1]
    dt = datetime.strptime(str_dt, '[%Y-%m-%d %H:%M]')

    # parse event
    str_ev = line[line.find(']') + 1:].strip()
    return ((dt, str_ev))

def logsIntoData(logs: [(datetime, str)]) -> {}:
    # create guard objects for each
    # id -> [(begin, end, duration)]
    guardSleeps = {}
    curGuard = None
    curSleep = None
    curWake = None
    for l in logs:
        dt = l[0]
        ev = l[1]
        #print("adding for {}, log {}".format(curGuard, l))
        if ev == 'wakes up':
            curWake = dt

            # add new
            dur = curWake.minute - curSleep.minute
            data = (curSleep.minute, curWake.minute, dur)
            if curGuard not in guardSleeps:
                guardSleeps[curGuard] = Guard(curGuard)
            guardSleeps[curGuard].addSleep(data)
            curSleep = None
        elif ev == 'falls asleep':
            curSleep = dt
        else:
            # new guard
            curGuard = int(ev[ev.find('#') + 1:ev.find('b') - 1])
    return guardSleeps

def task():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

        logs = []

        for l in lines:
            logs.append(parseLine(l))

        # sort datetime
        logs.sort()

        guardSleeps = logsIntoData(logs)

        # find biggest time asleep
        bigGuard = None
        bigTot = 0
        
        for g in guardSleeps:
            guard = guardSleeps[g]

            if guard.getTotSleep() > bigTot:
                bigGuard = guard
                bigTot = guard.getTotSleep()
        print('{} -> {}'.format(bigGuard.getStats(), bigGuard.id * bigGuard.getAvgMin()))
        
        f.close()

def tests():
    with open('input_tests.txt') as f:
        lines = f.readlines()

        logs = []
        for l in lines:
            logs.append(parseLine(l))
        logs.sort()

        guardSleeps = logsIntoData(logs)

        for g in guardSleeps:
            guard = guardSleeps[g]

            print(guard.getStats())

        f.close()

task()