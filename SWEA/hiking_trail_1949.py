def finder(value, i, j, count, times):
    global N, max_length, flag
    for d in range(4):
        x = i+dx[d]
        y = j+dy[d]
        if 0<=x<N and 0<=y<N:
            if maps[x][y] < value:
                finder(maps[x][y], x, y, count+1, times)
            elif maps[x][y]-K < value and times:
                finder(value-1, x, y, count+1, False)
    max_length = max(max_length, count)

# T = int(input())
T = 1
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for tc in range(1,T+1):
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    max_length = 0
    maxN = 0
    for i in range(N):
        maxN = max(maxN, max(maps[i]))
    for i in range(N):
        for j in range(N):
            if maps[i][j] == maxN:
                finder(maxN,i,j,1, True)
    print(max_length)