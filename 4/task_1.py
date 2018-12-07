from datetime import datetime
import operator

class Guard:
    def __init__(self, id: int):
        self.id = id
        # (begin, end, duration)
        self.sleeps = []
    
    def addSleep(self, sleep: (datetime, datetime, int)):
        self.sleeps.append(sleep)
    
    def getTotSleep(self):
        pass
    
    def getAvgMin(self):
        pass

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
                dur = (curWake - curSleep).seconds//60
                data = (curSleep, curWake, dur)
                if curGuard in guardSleeps:
                    guardSleeps[curGuard].append(data)
                else:
                    guardSleeps[curGuard] = [data]
            # new guard
            curGuard = int(ev[ev.find('#') + 1:ev.find('b') - 1])
    
    # find biggest time asleep
    # & average minute
    bigGuard = None
    bigSleep = 0
    bigAvgMin = None
    for id in guardSleeps:
        totSleep = 0
        mins = {}
        for sl in guardSleeps[id]:
            totSleep += sl[2]
            # calc avg min
            start = sl[0].minute
            finish = sl[1].minute
            for m in range(start, finish):
                if m in mins:
                    mins[m] += 1
                else:
                    mins[m] = 1
        if totSleep > bigSleep:
            bigGuard = id
            bigSleep = totSleep
            bigAvgMin = max(mins.items(), key=operator.itemgetter(1))[0]
            print("{}: {}, {}".format(bigGuard, bigSleep, bigAvgMin))
            
    print("{}: {}, {}".format(bigGuard, bigSleep, bigAvgMin))
    print("{}".format(bigGuard * bigAvgMin))
    
    f.close()