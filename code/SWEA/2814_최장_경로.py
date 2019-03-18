def DFS():
    

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Edges = [list(map(int, input().split())) for _ in range(M)]
    if not Edges:
        print(1)
    else:
        