from collections import deque

def BFS(i,j):
    global M, N
    direction = ((0,1),(1,0),(0,-1), (-1,0))
    queue = deque([(i,j)])
    while queue:
        n = queue.popleft()
        for d in direction:
            ni = d[0] + n[0]
            nj = d[1] + n[1]
            if 0<=ni<N and 0<=nj<M and board[ni][nj]:
                queue.append((ni, nj))
                board[ni][nj] = 0

def pprint():
    global M, N
    for i in range(N):
        print(*board[i])
    print()

def finder():
    global M, N
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                board[i][j] = 0
                BFS(i,j)
                cnt += 1
    return cnt


for _ in range(int(input())):
    # 가로 M, 세로 N, 배추개수 K
    M, N, K = map(int, input().split())
    # 가로 x, 세로 y
    cabbages = [list(map(int, input().split())) for _ in range(K)]
    board = [[0 for _ in range(M)] for _ in range(N)]
    for c in cabbages:
        board[c[1]][c[0]] = 1

    print(finder())