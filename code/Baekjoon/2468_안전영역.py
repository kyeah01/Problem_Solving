direction = ((0,1), (1,0), (0,-1), (-1,0))
def check(water):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j]-water>0 and not visited[i][j]:
                cnt += 1
                visited[i][j] = 1
                sink(water, (i,j), visited)
    return cnt

def sink(water, start, visited):
    queue = [start]
    e, i = 0, -1
    while e != i:
        i += 1
        n = queue[i]
        for d in direction:
            nx, ny = n[0]+d[0], n[1]+d[1]
            if 0<=nx<N and 0<=ny<N and maps[nx][ny]-water>0 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                e += 1

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

numbers = set()
maxHeight = max(maps[i][j] for i in range(N) for j in range(N))
safe = 1
for water in range(maxHeight, -1, -1):
    n = check(water)
    safe = max(safe, n)
print(safe)