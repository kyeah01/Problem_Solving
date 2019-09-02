def finder():
    global sero, garo
    result = 0
    for i in range(sero):
        for j in range(garo):
            if maps[i][j] == 'L':
                result = max(result, BFS((i,j,0)))
    return result

def BFS(start):
    global sero, garo
    queue = [start]
    visited = [(start[0], start[1])]
    direction = ((0,1), (1,0), (0,-1), (-1,0))
    times = 0
    while queue:
        n = queue.pop(0)
        times = max(times, n[2])
        for d in direction:
            nx, ny = n[0]+d[0], n[1]+d[1]
            if 0 <= nx < sero and 0 <= ny < garo and maps[nx][ny] == 'L' and (nx, ny) not in visited:
                queue += [(nx, ny, n[2]+1)]
                visited += [(nx, ny)]
    return times

sero, garo = map(int, input().split())
maps = [list(input()) for _ in range(sero)]
print(finder())