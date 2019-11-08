def solution(n, edge):
    edge_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for s, e in edge:
        edge_matrix[s-1][e-1] = 1
        edge_matrix[e-1][s-1] = 1
    nodes = [0 for _ in range(n)]
    queue = [0]
    nodes[0] = 1
    s,e = 0,1
    maxN = 1
    maxList = 0
    while s != e:
        now = queue[s]
        s += 1
        for i in range(n):
            if edge_matrix[now][i] and not nodes[i]:
                e += 1
                nodes[i] = nodes[now]+1
                queue += [i]
                if maxN == nodes[now]+1:
                    maxList += 1
                elif maxN < nodes[now]+1:
                    maxN = nodes[now]+1
                    maxList = 1
    return maxList