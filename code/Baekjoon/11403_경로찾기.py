def pprint():
    for i in range(N):
        print(*ans[i])

def DFS(visited):
    global N
    # 내가 갈 수 있는 곳은 내가 있는 번호줄의 1뿐임.
    # 마지막 노드는 visited[-1]
    flag = True
    for i in range(N):
        if edges[visited[-1]][i] and i not in visited[1:] and not ans[visited[-1]][i]:
            flag = False
            DFS(visited+[i])
    
    if flag:
        if visited[0] == visited[-1]:
            visited += visited[1:-1]
        for x in range(len(visited)):
            for y in range(x+1, len(visited)):
                ans[visited[x]][visited[y]] = 1

N = int(input())

edges = [list(map(int, input().split())) for _ in range(N)]
ans = [[0 for j in range(N)] for i in range(N)]

for i in range(N):
    for j in range(N):
        # 갈 수 있는 방향.
        if edges[i][j]:
            DFS([i,j])
pprint()