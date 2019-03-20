import sys
sys.stdin = open('input.txt')

def navi(i, j, time):
    global cnt
    if not time:
        return
    way = pipe[maps[i][j]]
    maps[i][j] = 0
    cnt += 1
    for d in range(len(way)):
        x = i+way[d][0]
        y = j+way[d][1]
        if 0<=x<N and 0<=y<M and maps[x][y] and [-way[d][0], -way[d][1]] in pipe[maps[x][y]]:
            navi(x,y,time-1)

pipe = {
    1 : [[-1,0],[0,1],[1,0],[0,-1]],
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
    cnt = 0
    navi(R,C,L)
    print(cnt)
    for i in range(N):
        print(*maps[i])