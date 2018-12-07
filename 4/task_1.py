from datetime import datetime
import operator

class Guard:
    def __init__(self, id: int, sleeps: []):
        self.id = id
        # (begin, end, duration)
        self.sleeps = []
    
    def addSleep(self, sleep: (datetime, datetime, int)) -> None:
        self.sleeps.append(sleep)
    
    def getTotSleep(self) -> int:
        tot = 0
        for s in self.sleeps:
            tot += s[2]
        return tot
    
    def getAvgMin(self) -> int:
        mins = {}
        for s in self.sleeps:
            begin = s[0].minute
            end = s[1].minute
            for m in range(begin, end):
                if m in mins:
                    mins[m] = mins[m] + 1
                else:
                    mins[m] = 1
        return max(mins.items(), key=operator.itemgetter(1))[0]

    def getStats(self) -> str:
        return "id:{}, tot:{}, min:{}".format(g, guardSleeps[g].getTotSleep(), guardSleeps[g].getAvgMin())

    def __str__(self):
        return "{}: {}".format(self.id, list(map(lambda x: "{}->{}".format(x[0], x[1]), self.sleeps)))

with open('input.txt', 'r') as f:
    lines = f.readlines()

    logs = []

    for l in lines:
        # parse datetime
        str_dt = l[:l.find(']') + 1]
        dt = datetime.strptime(str_dt, '[%Y-%m-%d %H:%M]')

        # parse event
        str_ev = l[l.find(']') + 1:].strip()

        logs.append((dt, str_ev))

    # sort datetime
    logs.sort()

    # create guard objects for each
    # id -> [(begin, end, duration)]
    guardSleeps = {}
    curGuard = None
    curSleep = None
    curWake = None
    for l in logs:
        dt = l[0]
        ev = l[1]
        if ev == 'wakes up':
            curWake = dt
        elif ev == 'falls asleep':
            curSleep = dt
        else:
            if curGuard != None:
                dur = (curWake - curSleep).seconds/60
                #print("{}->{} = {}".format(curSleep, curWake, dur))
                data = (curSleep, curWake, dur)

                if curGuard in guardSleeps:
                    guardSleeps[curGuard].addSleep(data)
                else:
                    guardSleeps[curGuard] = Guard(curGuard, [data])
            # new guard
            curGuard = int(ev[ev.find('#') + 1:ev.find('b') - 1])

    # find biggest time asleep
    bigGuard = None
    bigTot = 0
    for g in guardSleeps:
        guard = guardSleeps[g]
        if guard.getTotSleep() > bigTot:
            print('{} > {}'.format(guard.getTotSleep(), bigTot))
            bigGuard = guard
            bigTot = guard.getTotSleep()
        print(guard.getStats())
    print('---')
    print(bigGuard.getStats())
    
    f.close()