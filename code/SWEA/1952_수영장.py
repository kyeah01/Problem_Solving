T = int(input())

for tc in range(1, T+1):
    day, mon, t_mon, year = map(int, input().split())
    pay = {'day':day, 'mon':mon, 't_mon':t_mon, 'year':year}
    schedule = list(map(int, input().split()))
    calendar = schedule[:]

    for i in range(12):
        if schedule[i] >= mon//day:
            calendar[i] = 'mon'
    for i in range(10):
        if set(schedule[])