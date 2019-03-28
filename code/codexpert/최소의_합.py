# n개의 순열을 구하는 게임!
# 들어가는 숫자들은 0~n-1개!
import sys

def sumit(maps, n):
    arr = list(range(0,n))
    minN = sys.maxsize
    def permutation(n, k, total):
        nonlocal minN
        if n == k:
            if minN > total:
                minN = total
            return
        if minN <= total:
            return
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            permutation(n, k+1, total+maps[k][arr[k]])
            arr[i], arr[k] = arr[k], arr[i]
    permutation(n, 0, 0)

    return sum(min(maps[i]) for i in range(n)), minN

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
for x in sumit(maps, n):
    print(x)