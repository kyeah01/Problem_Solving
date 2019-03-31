def comb(k,total):
    global sol, target, n
    if total >= target:
        sol = min(sol, total-target)
        return
    if n == k:
        if total >= target:
            sol = min(sol, total-target)
        return
    comb(k+1,total+height[k])
    comb(k+1,total)

# main
T = int(input())
for _ in range(T):
    n, target = map(int, input().split())
    height = [int(input()) for _ in range(n)]
    arr = [0]*n
    sol = 10000000
    comb(0,0)
    print(sol)