def recursion_DFS(x, j):
    global ans
    flag = True
    print(Edges)
    for i in range(len(Edges)):
        if x == Edges[i][0]:
            flag = False
            recursion_DFS(Edges[i][1], i)
    if flag:
        ans += [x]
        Edges.pop(i)

for tc in range(1, 11):
    V, E = map(int, input().split())
    Egdes = list(map(int, input().split()))
    Edges = [[Egdes[i], Egdes[i+1]] for i in range(0, 2*E, 2)]
    ans = []
    recursion_DFS(Edges[0][0],0)
    print(ans)