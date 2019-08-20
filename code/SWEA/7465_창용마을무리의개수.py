import sys
sys.stdin = open('input.txt')

def pprint(graph):
    for g in graph:
        print(*g)
    print()

def DFS(start):
    visited = []
    stack = [start,]

    while stack:
        print('s', stack)
        print('v', visited)
        n = stack.pop()
        if n not in visited:
            visited += [n]
            print('to stack', [i for i, v in enumerate(graph[n]) if v], set([i for i, v in enumerate(graph[n]) if v]) - set(visited))
            stack += set([i for v, i in enumerate(graph[n]) if v]) - set(visited)
    visited += [n]
    return visited

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    edges = tuple(tuple(map(lambda x: int(x)-1, input().split())) for _ in range(M))
    
    # 인접 그래프 만들기
    graph = [[0 for _ in range(N)] for _ in range(N)]
    
    for edge in edges:
        graph[edge[0]][edge[1]] = 1
        graph[edge[1]][edge[0]] = 1
    
    # DFS하기
    cnt = 0
    visited = []
    for i in range(N):
        if i not in visited:
            visited += DFS(i)
            cnt += 1
        print('end')

    print(visited)
    print(cnt)