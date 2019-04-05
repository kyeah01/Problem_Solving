def dot(i,j):
    global first
    queue = [(i,j)]
    first += [(i,j)]
    while queue:
        i,j = queue.pop(0)
        for d in range(4):
            x = i+direction[d][0]
            y = j+direction[d][1]
            if 0<=x<n and 0<=y<m and leather[x][y] == 'X' and (x,y) not in first:
                queue += [(x,y)]
                first += [(x,y)]

def finder():
    for i in range(n):
        for j in range(m):
            if leather[i][j] == 'X':
                dot(i,j)
                return

def fastest(i,j):
    queue = [(i,j,0)]
    visited = []
    # print(queue)
    while queue:
        i,j,c = queue.pop(0)
        for d in range(4):
            x = i+direction[d][0]
            y = j+direction[d][1]
            if 0<=x<n and 0<=y<m and (x,y) not in visited:
                if leather[x][y] == '.':
                    queue += [(x,y,c+1)]
                    visited += [(x,y)]
                elif leather[x][y] == 'X' and (x,y) not in first:
                    return c
    return 101010101010

def solution():
    result = 0xffffff
    for i in range(len(first)):
        x,y = first[i]
        for d in range(4):
            nx = x+direction[d][0]
            ny = y+direction[d][1]
            if 0<=nx<n and 0<=ny<m and leather[nx][ny] == '.':
                # print(nx, ny)
                ans = fastest(x, y)
                result = min(result, ans)
    print(result)


direction = ((0,1), (1,0), (0,-1), (-1,0))
n, m = map(int, input().split())
leather = [list(input()) for _ in range(n)]
first = []
finder()
solution()


# 맨 처음 첫 점의 위치를 다 찾자.
# '.'을 인접한 점들만 BFS하게 만들자.
# 인접 점에서 부터 점을 쭉 따라가며 다음 X를 찾다가 만약 x를 만나면,
# 첫 점에 포함됐는지 아닌지를 판별하고, 아니라면 cnt를 저장한다.