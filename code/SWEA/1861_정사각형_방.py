def maze_start(N, cube):
    def maze_runner(i, j, val, time):
        for direction in range(4):
            x = i+d[direction]
            y = j+d[::-1][direction]
            if 0<=x<N and 0<=y<N and cube[x][y]-1 == val:
                return maze_runner(x,y,cube[x][y],time+1)
        return time+1

    times = [[maze_runner(i,j,cube[i][j],0) for j in range(N)] for i in range(N)]
    print(times)
    x, y = [0, 0]
    for i in range(N):
        for j in range(N):
            if times[x][y] < times[i][j]:
                x,y = i,j
            elif times[x][y] == times[i][j]:
                if cube[x][y] > cube[i][j]:
                    x,y = i, j
    return cube[x][y], times[x][y],
    

d = [0,0,-1,1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cube = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{tc}', *maze_start(N, cube))