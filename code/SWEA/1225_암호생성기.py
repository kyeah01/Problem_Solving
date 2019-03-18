for _ in range(10):
    tc = int(input())
    liszt = list(map(int, input().split()))
    nxt = 1
    while nxt > 0:
        for x in range(1, 6):
            nxt = liszt.pop(0)-x
            if nxt <= 0:
                liszt += [0]
                break
            liszt += [nxt]
    print(liszt)