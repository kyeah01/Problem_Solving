def solution(start, end):
    queue = [(start[0], start[1], 0, 3)]
    while queue:
        i,j, cnt, bomb = queue.pop(0)
        for d in range(4):
            x = i+direction[d][0]
            y = j+direction[d][1]
            if not 0<=x<x_size and 0<=y<y_size: continue
            if (x,y) == end:
                print(cnt+1)
                return
            if maps[x][y] == 1:
                continue
            if bomb and maps[x][y] == 2 and visited[x][y] < bomb:
                queue += [(x,y,cnt+1,bomb-1)]
                visited[x][y] = bomb-1
            elif not maps[x][y] and visited[x][y] < bomb:
                queue += [(x,y,cnt+1, bomb)]
                visited[x][y] = bomb

direction = [(0,1), (1,0), (0,-1), (-1,0)]
x_size, y_size = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(x_size)]
visited = [[0 for _ in range(y_size)] for _ in range(x_size)]
for i in range(x_size):
    for j in range(y_size):
        if maps[i][j] == 3:
            start = (i,j)
        elif maps[i][j] == 4:
            end = (i,j)
solution(start, end)