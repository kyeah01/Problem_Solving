def setting(i, j):
    for direction in range(8):
        x = i+way[direction][0]
        y = j+way[direction][1]
        while 0<=x<N and 0<=y<N:
            if not board[x][y]:
                board[x][y] = 1
            x += way[direction][0]
            y += way[direction][1]

way = [[-1,-1], [-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1]]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = 0
    while True:
        board = [[0 for _ in range(N)] for _ in range(N)]
        route = []
        for i in range(N):
            for j in range(N):
                if not board[i][j] and [i,j] != before:
                    route += [[i,j]]
                    break
            else:
                before = route.pop()
