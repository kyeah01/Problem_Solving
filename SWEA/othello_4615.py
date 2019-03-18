def change(i, j, color):
    global N
    maps[i][j] = color
    for d in range(8):
        x, y = i+dx[d], j+dy[d]
        if 0<=x<N and 0<=y<N:
            if maps[x][y] in {'W', 'B'} and maps[x][y] != color:
                while 0<=x<N and 0<=y<N:
                    if not maps[x][y]:
                        break
                    elif maps[x][y] == color:
                        while (x, y) != (i, j):
                            maps[x][y] = color
                            x -= dx[d]
                            y -= dy[d]
                        break
                    x += dx[d]
                    y += dy[d]

def check(N):
    a, b = 0, 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 'B':
                a += 1
            elif maps[i][j] == 'W':
                b += 1
    return a, b

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    maps = [[0 for _ in range(N)] for _ in range(N)]
    # 초기설정
    maps[N//2-1][N//2-1], maps[N//2-1][N//2], maps[N//2][N//2-1], maps[N//2][N//2]= 'W', 'B', 'B', 'W'
    for x in range(M):
        i, j, color = map(int, input().split())
        color = 'B' if color==1 else 'W'
        # placement(j-1, i-1, color)
        change(j-1, i-1, color)
        if x == N**2-1:
            print('#{}'.format(tc), *check(N))
            break
    else:
        print('#{}'.format(tc), *check(N))


# def change(i, j, color):
#     global N
#     for d in range(8):
#         x, y = i+dx[d], j+dy[d]
#         if 0<=x<N and 0<=y<N:
#             if maps[x][y] in {'W', 'B'} and maps[x][y] != color:
#                 while 0<=x<N and 0<=y<N:
#                     if not maps[x][y]:
#                         break
#                     elif maps[x][y] == color:
#                         while (x, y) != (i, j):
#                             maps[x][y] = color
#                             x -= dx[d]
#                             y -= dy[d]
#                         break
#                     x += dx[d]
#                     y += dy[d]

# def placement(i,j,color):
#     global N, Flag
#     for d in range(8):
#         x, y = i+dx[d], j+dy[d]
#         if 0<=x<N and 0<=y<N:
#             if maps[x][y] in {'W', 'B'} and maps[x][y] != color:
#                 while 0<=x<N and 0<=y<N:
#                     if not maps[x][y]:
#                         break
#                     elif maps[x][y] == color:
#                         maps[i][j] = color
#                         return change(i,j,color)
#                     x += dx[d]
#                     y += dy[d]
#     if color == 'W':
#         Flag[0] = 1
#     else:
#         Flag[1] = 1