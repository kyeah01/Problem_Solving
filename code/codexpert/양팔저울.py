def balance(k, right, left):
    global result, flag
    if n == k:
        if right == left:
            flag = True
        return 
    balance(k+1, right+weights[k], left)
    balance(k+1, right, left+weights[k])
    balance(k+1, right, left)

n = int(input())
weights = list(map(int, input().split()))
x = int(input())
marbles = list(map(int, input().split()))
result = []
for marble in marbles:
    flag = False
    balance(0, marble, 0)
    if flag:
        result += ['Y']
    else:
        result += ['N']
print(*result)