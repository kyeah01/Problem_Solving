N, M, V = map(int, input().split())

input_edges = [list(map(int, input().split())) for _ in range(M)]
edg = {x:[] for e in input_edges for x in e}

for i in range(M):
    edg[input_edges[i][0]] += [input_edges[i][1]]
    edg[input_edges[i][1]] += [input_edges[i][0]]

queue = [V]
BFS_visited = []

while queue:
    BFS_visited += [queue.pop(0)]
    queue += [e for e in edg[BFS_visited[-1]] if e not in BFS_visited and e not in queue]


stack = [V]
DFS_visited = []

while N > len(DFS_visited):
    if edg[stack[-1]]:
        if edg[stack[-1]][0] not in stack and edg[stack[-1]][0] not in DFS_visited:
            stack += [edg[stack[-1]].pop(0)]
        else:
            edg[stack[-1]].pop(0)
    else:
        DFS_visited += [stack.pop()]

print(*DFS_visited[::-1])
print(*BFS_visited)