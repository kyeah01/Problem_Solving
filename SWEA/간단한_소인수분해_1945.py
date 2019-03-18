import math

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x = N
    a,b,c,d,e = 0,0,0,0,0
    while not x%2:
        a += 1
        x //= 2
    while not x%3:
        b += 1
        x //= 3
    while not x%5:
        c += 1
        x //= 5
    while not x%7:
        d += 1
        x //= 7
    while not x%11:
        e += 1
        x //= 11
    print(a,b,c,d,e)