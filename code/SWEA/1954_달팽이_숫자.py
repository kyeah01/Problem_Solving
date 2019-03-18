T = int(input())
for tc in range(1, T+1):
    n = int(input())
    snail = [[0 for _ in range(n)] for _ in range(n)]
    way = [[0,1],[1,0],[0,-1],[-1,0]]
    num = 2
    i, j = 0, 0
    direction = 0
    snail[0][0] = 1
    while num < n*n+1:
        x = i+way[direction][0]
        y = j+way[direction][1]
        if 0<=x<n and 0<=y<n and not snail[x][y]:
            i, j = x, y
            snail[i][j] = num
            num += 1
        else:
            direction = (direction+1)%4
    
    # print(f'#{tc}')
    for i in range(n):
        print(*snail[i])