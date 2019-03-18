import sys
sys.setrecursionlimit(100000)

def DFS(i,j):
    # 재귀함수 사용
    global cnt, M, N
    dxy = [0,0,1,-1]
    field[i][j] = 0
    for k in range(4):
        if 0<=i+dxy[k]<M and 0<=j+dxy[::-1][k]<N and field[i+dxy[k]][j+dxy[::-1][k]]:
            DFS(i+dxy[k], j+dxy[::-1][k])

T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    field = [[0 for _ in range(N)] for _ in range(M)]
    state = [list(map(int, input().split())) for _ in range(K)]
    cnt = 0
    for s in state:
        field[s[0]][s[1]] = 1
    for x in range(M):
        for y in range(N):
            if field[x][y]:
                cnt += 1
                DFS(x,y)
    print(cnt)