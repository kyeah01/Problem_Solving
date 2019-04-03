def dice1(k):
    if k == n:
        print(*result)
        return
    for i in range(1,7):
        result[k] = i
        dice1(k+1)

def dice2(k, s):
    if k == n:
        print(*result)
        return 
    for i in range(s, 7):
        result[k] = i
        dice2(k+1, i+1)

def dice3(k):
    if k == n:
        print(*result)
        return 
    for i in range(1, 7):
        if i not in result[:k]:
            result[k] = i
            dice3(k+1)

n, m = map(int, input().split())
result = [0]*n
if m == 1:
    dice1(0)
elif m == 2:
    dice2(0,1)
else:
    dice3(0)