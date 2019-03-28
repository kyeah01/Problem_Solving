import sys

def permu_price(k, total_cost):
    global n, minN
    if n == k:
        if minN > total_cost:
            minN = total_cost
        return
    if total_cost > minN:
        return
    for i in range(k, n):
        arr[i], arr[k] = arr[k], arr[i]
        permu_price(k+1, total_cost+prices[k][arr[k]])
        arr[i], arr[k] = arr[k], arr[i]


# main
n = int(input())
prices = [list(map(int, input().split())) for _ in range(n)]
minN = sys.maxsize
arr = list(range(0, n))
permu_price(0, 0)
print(minN)