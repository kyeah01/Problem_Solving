def navi(value, i, j, time):
    global pipe, N, M
    if not time:
        return 
    way = pipe[value]
    for d in range(len(way)):
        x = i+way[d][0]
        y = j+way[d][1]
        print(x,y)
        # range over가 나지 않으면서, maps[x][y]가 0이 아니면서, 두 파이프가 연결된 경우. 
        if 0<=x<N and 0<=y<M and maps[x][y] and [-way[d][0], -way[d][1]] in pipe[maps[x][y]]:
            if not check[x][y]:
                check[x][y] = 'v'
                return navi(maps[x][y],x,y,time-1)

pipe = {
    1 : [[0,1],[1,0],[0,-1],[-1,0]],
    2 : [[-1,0],[1,0]],
    3 : [[0, -1], [0, 1]],
    4 : [[-1, 0],[0,1]],
    5 : [[1, 0],[0, 1]],
    6 : [[0, -1],[1, 0]],
    7 : [[0, -1],[-1, 0]]
}

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    print(maps)
    check = [[0 for _ in range(M)] for _ in range(N)]
    check[R][C] = 'v'
    navi(maps[R][C],R,C,L)
    for i in range(N):
        print(*check[i])