def solution():
    queue = [(0,0)]
    while queue:
        # print(visited)
        i,j = queue.pop(0)
        # print(i,j,visited[i][j],queue)
        for d in range(4):
            x = i+direct[d][0]
            y = j+direct[d][1]
            if 0<=x<n and 0<=y<n:
                if visited[x][y] > visited[i][j]+maps[x][y]:
                    queue += [(x,y)]
                    visited[x][y] = visited[i][j]+maps[x][y]
    print(visited[n-1][n-1])
    return visited[n-1][n-1]

direct = [(0,1), (0,-1), (1,0), (-1,0)]

n = int(input())
maps = [list(map(int, input())) for _ in range(n)]
visited = [[0xffffff for _ in range(n)] for _ in range(n)]
visited[0][0] = maps[0][0]
# print(visited)
solution()