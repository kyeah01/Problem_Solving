# 1에서 출발하고, 1로 도착하는 경로이니 유의해야 함.
def permu(k, now, total, went):
    global minN
    if len(went)==n-1:
        if costs[now][0]:
            minN = min(minN, total+costs[now][0])
            print(went)
        return
    if k == n:
        return
    if minN < total:
        return
    for i in range(1, n):
        # 방문했던 지역이 아니고, 방문할 수 없는 지역이 아닐때.
        if not chk[i] and costs[now][i]:
            chk[i] = 1
            permu(k+1, i, total+costs[now][i], went+[i])
            chk[i] = 0

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
chk = [0]*n
minN = 0xffffff
permu(0, 0, 0, [])
print(minN)