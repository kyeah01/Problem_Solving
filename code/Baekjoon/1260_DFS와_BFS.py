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

print(BFS_visited)

stack = [V]
DFS_visited = []

# while True:
    