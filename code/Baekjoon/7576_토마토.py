from collections import deque

direction = ((0,1), (1,0), (0, -1), (-1, 0))

def setting():
    global N, M
    start = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                start += [[i,j,0]]
    BFS(start)


def BFS(start):
    global N, M
    queue = deque(start)
    while queue:
        n = queue.popleft()
        for d in direction:
            nx = n[0]+d[0]
            ny = n[1]+d[1]
            if 0<= nx <N and 0<= ny <M and board[nx][ny] == 0:
                board[nx][ny] = 1
                queue.append((nx, ny, n[2]+1))
    print(n[2]) if check() else print(-1)

def check():
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                return False
    return True

# M은 가로, N은 세로
M,N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
setting()

# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸

# BFS로 토마토를 익히자!