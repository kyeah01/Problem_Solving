def timeCalc(time, interval):
    hour, minuite = time
    minuite += int(interval)
    if minuite >= 60:
        hour += 1
        minuite -= 60
    elif minuite < 0:
        hour -= 1
        minuite += 60
    return (hour, minuite)
        
def busTimeGenerator(cnt, interval):
    time = (9,0)
    for c in range(cnt):
        yield time
        time = timeCalc(time, interval)

def strToTime(string):
    return tuple(map(int, string.split(':')))

def timeToStr(time):
    hour = '0' * (2-len(str(time[0]))) + str(time[0])
    miniute = '0' * (2-len(str(time[1]))) + str(time[1])
    return hour + ':' + miniute

def checker(bus, passenger):
    if bus < passenger:
        return False
    return True

def solution(n, t, m, timetable):
    timetable.sort()
    queue = 0
    i = 0
    lastPassenger = 0
    for busTime in busTimeGenerator(int(n), t):
        leftSeats = m
        while i < len(timetable):
            if checker(busTime, strToTime(timetable[i])) and leftSeats:
                lastPassenger = i
                leftSeats -= 1
                i += 1
            else:
                break
    if busTime >= strToTime(timetable[lastPassenger]):
        if leftSeats:
            return timeToStr(busTime)
        return timeToStr(timeCalc(strToTime(timetable[lastPassenger]), -1))
    if busTime < strToTime(timetable[lastPassenger]):
        return timeToStr(busTime)
    return timeToStr(busTime)