T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] != '0':
                