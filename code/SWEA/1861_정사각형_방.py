def finder(cube, N):
    def guide(x, y):
        for k in range(4):
            nx, ny = x+d[k], x+d[::-1][k]
            if not 0<=nx<N or not 0<=ny<N:
                return 
            if 
    # 재귀를 돌면서 갈 수 있으면 간다.

    for i in range(N):
        for j in range(N):

    

d = [0,0,-1,1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cube = [list(map(int,input().split())) for _ in range(N)]
